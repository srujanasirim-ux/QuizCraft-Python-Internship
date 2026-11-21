import app as quiz_app
from models import Deck
def sample_decks():
    """Create a small sample deck for testing."""
    questions = [
        {
            "text": "Which keyword defines a function in Python?",
            "answer": "B",
            "choices": {
                "A": "function",
                "B": "def",
                "C": "define",
                "D": "fun"
            }
        }
    ]
    return {
        "Python": Deck("Python", questions)
    }
def test_home_page():
    """Check whether the home page loads."""
    client = quiz_app.app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"QUIZCRAFT" in response.data
def test_start_quiz(monkeypatch):
    """Check whether a quiz starts successfully."""
    monkeypatch.setattr(
        quiz_app,
        "load_decks",
        sample_decks
    )
    client = quiz_app.app.test_client()
    response = client.post(
        "/start/Python",
        data={"player_name": "Srujana"}
    )
    assert response.status_code == 302
    quiz_response = client.get("/play/Python")
    assert quiz_response.status_code == 200
    assert b"Which keyword defines a function" in quiz_response.data
def test_correct_answer(monkeypatch):
    """Check whether a correct answer increases the score."""
    monkeypatch.setattr(
        quiz_app,
        "load_decks",
        sample_decks
    )
    saved_results = []
    monkeypatch.setattr(
        quiz_app,
        "save_progress",
        lambda player, result: saved_results.append((player, result))
    )
    client = quiz_app.app.test_client()
    client.post(
        "/start/Python",
        data={"player_name": "Srujana"}
    )
    response = client.post(
        "/play/Python",
        data={"answer": "B"}
    )
    assert response.status_code == 302
    result_response = client.get("/results")
    assert result_response.status_code == 200
    assert b"1 / 1" in result_response.data
    assert len(saved_results) == 1
    assert saved_results[0][1]["score"] == 1
def test_result_saved_only_once(monkeypatch):
    """Check whether refreshing results avoids duplicate saving."""
    monkeypatch.setattr(
        quiz_app,
        "load_decks",
        sample_decks
    )
    saved_results = []
    monkeypatch.setattr(
        quiz_app,
        "save_progress",
        lambda player, result: saved_results.append(result)
    )
    client = quiz_app.app.test_client()
    client.post(
        "/start/Python",
        data={"player_name": "Srujana"}
    )
    client.post(
        "/play/Python",
        data={"answer": "B"}
    )
    client.get("/results")
    client.get("/results")
    client.get("/results")
    assert len(saved_results) == 1
def test_statistics_page(monkeypatch):
    """Check whether the statistics page displays saved results."""
    monkeypatch.setattr(
        quiz_app,
        "get_player_progress",
        lambda player: [
            {
                "deck": "Python",
                "score": 4,
                "total": 5,
                "date": "2026-11-21T20:00:00"
            }
        ]
    )
    client = quiz_app.app.test_client()
    response = client.get("/stats?player_name=Srujana")
    assert response.status_code == 200
    assert b"Python" in response.data
    assert b"4 / 5" in response.data