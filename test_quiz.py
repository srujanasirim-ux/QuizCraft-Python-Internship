from quiz import load_questions
import os
def test_load_questions():
    """Test whether questions are loaded correctly."""
    with open("test_questions.txt", "w", encoding="utf-8") as file:
        file.write("What is Python?|Programming Language\n")
        file.write("Which keyword defines a function?|def\n")
    questions = load_questions("test_questions.txt")
    assert len(questions) == 2
    assert questions[0]["question"] == "What is Python?"
    assert questions[0]["answer"] == "Programming Language"
    os.remove("test_questions.txt")
def test_load_questions_with_invalid_lines():
    """Test loading a file containing invalid and empty lines."""
    with open("test_questions.txt", "w", encoding="utf-8") as file:
        file.write("What is Python?|Programming Language\n")
        file.write("Invalid question without separator\n")
        file.write("|\n")
        file.write("\n")
    questions = load_questions("test_questions.txt")
    assert len(questions) == 1
    assert questions[0]["question"] == "What is Python?"
    os.remove("test_questions.txt")
def test_missing_file():
    """Test whether a missing file returns an empty list."""
    questions = load_questions("missing_questions.txt")
    assert questions == []