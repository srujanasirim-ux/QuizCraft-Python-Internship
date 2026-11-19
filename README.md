# QuizCraft – Python Quiz Trainer

## About the Project

QuizCraft is a beginner-friendly, terminal-based quiz application developed using Python. It allows users to practice quiz questions, organize questions into different decks, track their performance, and save their progress.

The project is developed as part of the SkillMe Python Internship and is completed in weekly stages.

## Features

### Week 1 – Terminal Quiz from a Text File
- Loads questions from `questions.txt`.
- Supports multiple quiz questions.
- Randomizes the order of questions.
- Checks answers without case sensitivity.
- Displays correct answers for incorrect responses.
- Shows final score, percentage, and wrong answers.
- Allows users to play multiple rounds.
- Handles invalid user input.
- Includes basic automated tests using pytest.

### Week 2 – Decks, Classes and Saved Progress
- Organizes questions into different quiz decks, such as Python and DSA.
- Uses Python classes: `Question`, `Deck`, and `QuizSession`.
- Supports multiple-choice questions with A, B, C, and D options.
- Allows players to choose a quiz deck.
- Saves each player's quiz results in `progress.json`.
- Tracks the number of attempts and best score for each deck.
- Maintains separate progress for different players.
- Automatically creates progress storage when results are first saved.
- Displays a menu to play quizzes, view statistics, or exit.

## Project Structure

```text
QuizCraft-Python-Internship/
│
├── quiz.py
├── questions.txt
├── test_quiz.py
│
├── models.py
├── storage.py
├── main.py
│
├── decks.json
├── progress.json       # Automatically generated
│
└── README.md
```

## Requirements

- Python 3.x
- pytest (for running Week 1 tests)
- No external libraries required for the main application.

## How to Run

### Week 1 – Terminal Quiz

Run the following command:

```bash
python quiz.py
```

Enter the number of questions you want to attempt, answer the questions, and view your final score.

### Week 2 – QuizCraft with Decks and Saved Progress

Run the following command:

```bash
python main.py
```

Enter your player name and choose an option from the main menu:

1. Play Quiz
2. View Statistics
3. Exit

Select a deck, answer the questions, and view your performance. Your progress is automatically saved and can be accessed when you run the application again.

## How to Add Questions

### Week 1

Open `questions.txt` and add questions using this format:

```text
Question|Answer
```

Example:

```text
What is the extension of a Python file?|.py
Which keyword defines a function in Python?|def
```

Make sure each question and answer is separated by the `|` symbol.

### Week 2

Open `decks.json` and add questions to an existing deck or create a new deck.

Each question contains:
- `text` – The question.
- `answer` – The correct answer.
- `choices` – Multiple-choice options.

## Technologies Used

- Python
- JSON
- File Handling
- Object-Oriented Programming (OOP)
- Classes and Methods
- Exception Handling
- Random Module
- Pytest

## Testing

Week 1 includes automated tests for question loading and file handling.

Run the tests using:

```bash
python -m pytest -v
```

## Learning Outcomes

Through this project, I practiced:

- Python functions and modular programming.
- File handling and exception handling.
- User input validation.
- Object-Oriented Programming.
- Creating and using Python classes.
- Reading and writing JSON files.
- Saving and retrieving player progress.
- Writing basic automated tests using pytest.

## Internship

**SkillMe – Python Virtual Internship**

- Week 1: Terminal Quiz from a Text File.
- Week 2: Decks, Classes and Saved Progress.

**Project:** QuizCraft – Python Quiz Trainer