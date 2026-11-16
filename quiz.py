import random
def load_questions(path):
    questions = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if "|" in line:
                    question, answer = line.split("|", 1)
                    question = question.strip()
                    answer = answer.strip()
                    if question and answer:
                        questions.append({
                            "question": question,
                            "answer": answer
                        })
    except FileNotFoundError:
        print("Error: Questions file not found!")
    return questions
def ask_question(q):
    print("\n" + q["question"])
    user_answer = input("Your answer: ").strip()
    correct_answer = q["answer"]
    if user_answer.lower() == correct_answer.lower():
        print("Correct answer!")
        return True, user_answer
    print("Wrong answer!")
    print("Correct answer:", correct_answer)
    return False, user_answer
def show_score(score, total, wrong_answers):
    percentage = (score / total) * 100 if total > 0 else 0
    print("\n========== QUIZ RESULTS ==========")
    print("Total Questions:", total)
    print("Correct Answers:", score)
    print("Incorrect Answers:", len(wrong_answers))
    print("Final Score:", score, "/", total)
    print("Percentage:", round(percentage, 2), "%")
    if wrong_answers:
        print("\nQuestions answered incorrectly:")
        for item in wrong_answers:
            print("\nQuestion:", item["question"])
            print("Your Answer:", item["your_answer"])
            print("Correct Answer:", item["correct_answer"])
    else:
        print("\nExcellent! All answers are correct!")
def main():
    print("================================")
    print("       PYTHON QUIZCRAFT")
    print("================================")
    questions = load_questions("questions.txt")
    if not questions:
        print("No valid questions available.")
        return
    print("\nAvailable Questions:", len(questions))
    while True:
        try:
            total = int(input("How many questions do you want? "))
            if 1 <= total <= len(questions):
                break
            print("Enter a number between 1 and", len(questions))
        except ValueError:
            print("Please enter a valid number.")
    random.shuffle(questions)
    selected_questions = questions[:total]
    score = 0
    wrong_answers = []
    for q in selected_questions:
        is_correct, user_answer = ask_question(q)
        if is_correct:
            score += 1
        else:
            wrong_answers.append({
                "question": q["question"],
                "your_answer": user_answer,
                "correct_answer": q["answer"]
            })
    show_score(score, total, wrong_answers)
if __name__ == "__main__":
    main()