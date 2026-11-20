import requests
import random
import html
API_URL = "https://opentdb.com/api.php"
def fetch_questions(amount, category=None, difficulty=None):
    """Fetch multiple-choice questions from the Open Trivia Database."""
    params = {
        "amount": amount,
        "type": "multiple"
    }
    if category:
        params["category"] = category
    if difficulty:
        params["difficulty"] = difficulty
    try:
        response = requests.get(
            API_URL,
            params=params,
            timeout=10
        )
        response.raise_for_status()
        data = response.json()
        if data.get("response_code") != 0:
            raise ValueError(
                "API could not provide questions. Please try again."
            )
        questions = []
        for item in data["results"]:
            question_text = html.unescape(item["question"])
            correct_answer = html.unescape(item["correct_answer"])
            incorrect_answers = [
                html.unescape(answer)
                for answer in item["incorrect_answers"]
            ]
            options = incorrect_answers + [correct_answer]
            random.shuffle(options)
            choices = {
                chr(65 + index): option
                for index, option in enumerate(options)
            }
            correct_letter = next(
                key for key, value in choices.items()
                if value == correct_answer
            )
            question = {
                "text": question_text,
                "answer": correct_letter,
                "choices": choices
            }
            questions.append(question)
        return questions
    except requests.exceptions.Timeout:
        raise RuntimeError("The API request timed out.")
    except requests.exceptions.RequestException:
        raise RuntimeError(
            "Unable to connect to the API. Check your internet connection."
        )
    except (KeyError, TypeError, ValueError) as error:
        raise RuntimeError(
            f"Unable to process API questions: {error}"
        )