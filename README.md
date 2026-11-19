# QuizCraft – Python Quiz Trainer

## About the Project
QuizCraft is a beginner-friendly, terminal-based quiz application developed using Python. It loads questions from a text file, asks users questions, checks their answers, and displays their final performance.

## Features
- Loads questions from `questions.txt`.
- Supports multiple quiz questions.
- Randomizes the order of questions.
- Checks answers without case sensitivity.
- Displays correct answers for incorrect responses.
- Shows final score, percentage, and wrong answers.
- Allows users to play multiple rounds.
- Handles invalid user input.

## Project Structure

```text
QuizCraft-Python-Internship/
│
├── quiz.py
├── questions.txt
└── README.md
```

## Requirements
- Python 3.x
- No external libraries required.

## How to Run

1. Clone or download this repository.
2. Open the project folder in VS Code or a terminal.
3. Run the following command:

```bash
python quiz.py
```

4. Enter the number of questions you want to attempt.
5. Answer the questions and view your final score.

## How to Add Questions

Open `questions.txt` and add new questions using this format:

```text
Question|Answer
```

Example:

```text
What is the extension of a Python file?|.py
Which keyword defines a function in Python?|def
```

Make sure each question and answer is separated by the `|` symbol.

## Technologies Used
- Python
- File Handling
- Functions
- Random Module

## Learning Outcomes
Through this project, I practiced Python functions, file handling, exception handling, user input validation, and basic application development.

## Internship
Week 1 Task – Python Internship  
Project: QuizCraft – Terminal Quiz from a Text File
