from datetime import datetime
class Question:

    def __init__(self, text, answer, choices=None):
        self.text = text
        self.answer = answer
        self.choices = choices
    def check(self, user_answer):

        if self.choices:
            return user_answer.strip().upper() == self.answer.upper()

        return user_answer.strip().lower() == self.answer.strip().lower()
#
#if __name__ == "__main__":
#    q1 = Question(
#        "Which keyword defines a function in Python?",
#        "B",
#        {"A": "function", "B": "def", "C": "define", "D": "fun"}
#    )
#    print(q1.check("b"))
#    print(q1.check("A"))
#    q2 = Question("What is the extension of a Python file?", ".py")
#    print(q2.check(".PY"))
#    print(q2.check(".java"))
class Deck:
    def __init__(self, name, questions_data):
        self.name = name
        self.questions = []
        for q in questions_data:
            question = Question(
                q["text"],
                q["answer"],
                q.get("choices")
            )
            self.questions.append(question)
    def get_questions(self):
        return self.questions
class QuizSession:
    def __init__(self, player_name, deck):
        self.player_name = player_name
        self.deck = deck
        self.score = 0
    def run(self):
        print("\n========== QUIZ STARTED ==========")
        print("Player:", self.player_name)
        print("Deck:", self.deck.name)
        questions = self.deck.get_questions()
        for question in questions:
            print("\n" + question.text)
            if question.choices:
                for key, value in question.choices.items():
                    print(key + ")", value)
                user_answer = input("Enter your option: ").strip()
            else:
                user_answer = input("Your answer: ").strip()
            if question.check(user_answer):
                print("Correct answer!")
                self.score += 1
            else:
                print("Wrong answer!")
                print("Correct answer:", question.answer)
        total = len(questions)
        print("\n========== QUIZ RESULTS ==========")
        print("Player:", self.player_name)
        print("Deck:", self.deck.name)
        print("Score:", self.score, "/", total)
        result = {
            "deck": self.deck.name,
            "score": self.score,
            "total": total,
            "date": datetime.now().isoformat(timespec="seconds")
        }
        return result
import json
if __name__ == "__main__":
    with open("decks.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    python_data = data["Python"]["questions"]
    python_deck = Deck("Python", python_data)
    print("Deck Name:", python_deck.name)
    print("Total Questions:", len(python_deck.get_questions()))
    for q in python_deck.get_questions():
        print("\nQuestion:", q.text)
        print("Correct Answer:", q.answer)
    session = QuizSession("Srujana", python_deck)
    result = session.run()
    print("\nReturned Result:")
    print(result)