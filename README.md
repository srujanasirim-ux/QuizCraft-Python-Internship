
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

### Week 3 – Import Questions from a Free API

- Integrates the Open Trivia Database (OpenTDB) API to fetch online quiz questions.
- Allows players to select quiz categories such as General Knowledge, Science & Nature, Computers, Mathematics, Sports, History, and Geography.
- Supports Easy, Medium, and Hard difficulty levels.
- Allows players to choose the number of questions (5–10).
- Converts API responses into the existing multiple-choice question format.
- Decodes HTML entities in fetched questions and answers.
- Randomizes answer choices.
- Uses the existing `QuizSession` class to conduct online quizzes.
- Handles API errors, connection failures, and request timeouts.
- Automatically provides local quiz decks when the API is unavailable.
- Allows players to save fetched online questions as new local decks for offline practice.
- Saves online and offline quiz results in player progress.

## Project Structure

```text
QuizCraft-Python-Internship/
│
├── quiz.py
├── questions.txt
├── test_quiz.py
│
├── api.py
├── models.py
├── storage.py
├── main.py
│
├── decks.json
├── progress.json       # Automatically generated
│
├── .gitignore
└── README.md
```

## Requirements

- Python 3.x
- requests
- pytest (for running Week 1 tests)

## Installation

Install the required libraries using:

```bash
pip install requests pytest
```

## How to Run

### Week 1 – Terminal Quiz

Run:

```bash
python quiz.py
```

Enter the number of questions you want to attempt, answer the questions, and view your final score.

### Week 2 and Week 3 – QuizCraft Application

Run:

```bash
python main.py
```

Enter your player name and choose an option from the main menu:

1. Play Local Quiz
2. Online Quiz
3. View Statistics
4. Exit

**Play Local Quiz:**

- Select an available quiz deck.
- Answer multiple-choice questions.
- View your final score.
- Your progress is automatically saved.

**Online Quiz:**

- Select a category.
- Choose a difficulty level.
- Select the number of questions.
- Answer the fetched questions.
- Optionally save the questions as a new local deck.

If the API is unavailable, QuizCraft automatically switches to local quiz decks so players can continue practicing.

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

### Week 2 and Week 3

Open `decks.json` and add questions to an existing deck or create a new deck.

Each question contains:

- `text` – The question.
- `answer` – The correct answer option.
- `choices` – Multiple-choice options.

Online questions can also be saved directly as new local decks through the application.

## Technologies Used

- Python
- Open Trivia Database API
- REST API Integration
- Requests Library
- JSON
- File Handling
- Object-Oriented Programming (OOP)
- Classes and Methods
- Exception Handling
- Random Module
- HTML Entity Decoding
- Pytest

## Testing

Week 1 includes automated tests for question loading and file handling.

Run the tests using:

```bash
python -m pytest -v
```

Week 2 and Week 3 features were also tested manually, including:

- Playing local quiz decks.
- Saving and retrieving player progress.
- Viewing quiz statistics.
- Fetching online questions using different categories and difficulty levels.
- Saving online questions as local decks.
- Playing saved decks offline.
- Testing API connection failure and local fallback.

## Learning Outcomes

Through this project, I practiced:

- Python functions and modular programming.
- File handling and exception handling.
- User input validation.
- Object-Oriented Programming.
- Creating and using Python classes.
- Reading and writing JSON files.
- Saving and retrieving player progress.
- Working with REST APIs.
- Sending HTTP requests using the Requests library.
- Handling API responses and network errors.
- Converting external API data into application-specific formats.
- Writing basic automated tests using pytest.

## Internship

**SkillMe – Python Virtual Internship**

- Week 1: Terminal Quiz from a Text File.
- Week 2: Decks, Classes and Saved Progress.
- Week 3: Import Questions from a Free API.

**Project:** QuizCraft – Python Quiz Trainer
```

### Next step

1. Open `README.md`.
2. Replace its contents with the updated version.
3. Save using `Ctrl + S`.

Then tell me when it's saved. We'll check the project files and run the Week 1 automated tests before committing Week 3 to GitHub.