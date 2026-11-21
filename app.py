import json
import os
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, session
from models import Deck, Question
from storage import save_progress, get_player_progress
app = Flask(__name__)
app.secret_key = os.environ.get(
    "SECRET_KEY",
    "quizcraft-development-secret-key"
)
def load_decks():
    """Load quiz decks from decks.json."""
    with open("decks.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    decks = {}
    for deck_name, deck_data in data.items():
        decks[deck_name] = Deck(
            deck_name,
            deck_data["questions"]
        )
    return decks
@app.route("/")
def home():
    """Display all available quiz decks."""
    try:
        decks = load_decks()
    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        decks = {}
    return render_template(
        "index.html",
        deck_names=list(decks.keys())
    )
@app.route("/start/<deck_name>", methods=["POST"])
def start_quiz(deck_name):
    """Start a new quiz for the selected deck."""
    player_name = request.form.get("player_name", "").strip()
    if not player_name:
        return redirect(url_for("home"))
    try:
        decks = load_decks()
    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        return redirect(url_for("home"))
    if deck_name not in decks:
        return redirect(url_for("home"))
    selected_deck = decks[deck_name]
    if not selected_deck.questions:
        return redirect(url_for("home"))
    questions = []
    for question in selected_deck.get_questions():
        questions.append({
            "text": question.text,
            "answer": question.answer,
            "choices": question.choices
        })
    session["quiz"] = {
        "player_name": player_name,
        "deck_name": deck_name,
        "questions": questions,
        "current_index": 0,
        "score": 0,
        "wrong_answers": [],
        "result_saved": False
    }
    return redirect(url_for("play_quiz", deck_name=deck_name))
@app.route("/play/<deck_name>", methods=["GET", "POST"])
def play_quiz(deck_name):
    """Display and process one question at a time."""
    quiz = session.get("quiz")
    if not quiz or quiz["deck_name"] != deck_name:
        return redirect(url_for("home"))
    questions = quiz["questions"]
    current_index = quiz["current_index"]
    if current_index >= len(questions):
        return redirect(url_for("results"))
    question_data = questions[current_index]
    if request.method == "POST":
        user_answer = request.form.get("answer", "").strip()
        question = Question(
            question_data["text"],
            question_data["answer"],
            question_data.get("choices")
        )
        if question.check(user_answer):
            quiz["score"] += 1
        else:
            quiz["wrong_answers"].append({
                "text": question_data["text"],
                "your_answer": user_answer,
                "correct_answer": question_data["answer"],
                "choices": question_data.get("choices")
            })
        quiz["current_index"] += 1
        session["quiz"] = quiz
        return redirect(url_for("play_quiz", deck_name=deck_name))
    return render_template(
        "quiz.html",
        quiz=quiz,
        question=question_data,
        question_number=current_index + 1,
        total=len(questions)
    )
@app.route("/results")
def results():
    """Display quiz results and save progress once."""
    quiz = session.get("quiz")
    if not quiz:
        return redirect(url_for("home"))
    if quiz["current_index"] < len(quiz["questions"]):
        return redirect(
            url_for("play_quiz", deck_name=quiz["deck_name"])
        )
    if not quiz["result_saved"]:
        result = {
            "deck": quiz["deck_name"],
            "score": quiz["score"],
            "total": len(quiz["questions"]),
            "date": datetime.now().isoformat(timespec="seconds")
        }
        save_progress(quiz["player_name"], result)
        quiz["result_saved"] = True
        session["quiz"] = quiz
    return render_template(
        "results.html",
        quiz=quiz,
        total=len(quiz["questions"])
    )
@app.route("/stats")
def stats():
    """Display attempts and best scores for a player."""
    player_name = request.args.get("player_name", "").strip()
    if not player_name:
        return render_template(
            "stats.html",
            player_name="",
            statistics=[]
        )
    results = get_player_progress(player_name)
    statistics = []
    deck_names = set(
        result["deck"] for result in results
    )
    for deck_name in sorted(deck_names):
        deck_results = [
            result for result in results
            if result["deck"] == deck_name
        ]
        statistics.append({
            "deck": deck_name,
            "attempts": len(deck_results),
            "best_score": max(
                result["score"] for result in deck_results
            ),
            "total": deck_results[0]["total"]
        })
    return render_template(
        "stats.html",
        player_name=player_name,
        statistics=statistics
    )
if __name__ == "__main__":
    app.run(debug=True)