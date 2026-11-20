import json
import os
from models import Deck, QuizSession
from storage import save_progress, get_player_progress
from api import fetch_questions
def load_decks():
    """Load all quiz decks from the JSON file."""
    with open("decks.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    decks = {}
    for deck_name, deck_data in data.items():
        decks[deck_name] = Deck(deck_name, deck_data["questions"])
    return decks
def save_deck(deck_name, questions):
    """Save online questions as a new local deck."""
    try:
        with open("decks.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        if deck_name in data:
            print("A deck with this name already exists.")
            return False
        data[deck_name] = {"questions": questions}
        with open("decks.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        print("Online questions saved as a local deck!")
        return True
    except (OSError, json.JSONDecodeError) as error:
        print("Unable to save deck:", error)
        return False
def show_stats(player_name):
    """Display attempts and best score for each deck."""
    results = get_player_progress(player_name)
    if not results:
        print("\nNo quiz attempts found yet.")
        return
    print("\n========== YOUR STATISTICS ==========")
    for deck_name in set(result["deck"] for result in results):
        deck_results = [
            result for result in results
            if result["deck"] == deck_name
        ]
        attempts = len(deck_results)
        best_score = max(
            result["score"] for result in deck_results
        )
        total = deck_results[0]["total"]
        print("\nDeck:", deck_name)
        print("Attempts:", attempts)
        print("Best Score:", best_score, "/", total)
def play_deck(player_name, selected_deck):
    """Run a quiz and save the player's result."""
    session = QuizSession(player_name, selected_deck)
    result = session.run()
    save_progress(player_name, result)
    print("\nYour progress has been saved!")
def online_quiz(player_name, decks):
    """Fetch and play questions from the online API."""
    print("\n========== ONLINE QUIZ ==========")
    print("\nChoose Category:")
    print("1. General Knowledge")
    print("2. Science & Nature")
    print("3. Computers")
    print("4. Mathematics")
    print("5. Sports")
    print("6. History")
    print("7. Geography")
    print("8. Any Category")
    category_options = {
        "1": 9,
        "2": 17,
        "3": 18,
        "4": 19,
        "5": 21,
        "6": 23,
        "7": 22,
        "8": None
    }
    category_choice = input("Enter your choice: ").strip()
    if category_choice not in category_options:
        print("Invalid category choice.")
        return
    category = category_options[category_choice]
    print("\nChoose Difficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    difficulty_options = {
        "1": "easy",
        "2": "medium",
        "3": "hard"
    }
    difficulty_choice = input("Enter your choice: ").strip()
    if difficulty_choice not in difficulty_options:
        print("Invalid difficulty choice.")
        return
    difficulty = difficulty_options[difficulty_choice]
    try:
        amount = int(input("How many questions? (5-10): "))
        if not 5 <= amount <= 10:
            print("Please enter a number between 5 and 10.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    print("\nFetching online questions...")
    try:
        questions = fetch_questions(
            amount,
            category,
            difficulty
        )
        if not questions:
            raise RuntimeError(
                "No questions were returned by the API."
            )
        print("\nSuccessfully fetched", len(questions), "questions!")
        online_deck = Deck("Online Quiz", questions)
        play_deck(player_name, online_deck)
        save_choice = input(
            "\nDo you want to save these questions as a local deck? (yes/no): "
        ).strip().lower()
        if save_choice in ("yes", "y"):
            deck_name = input(
                "Enter a name for the new deck: "
            ).strip()
            if deck_name:
                if save_deck(deck_name, questions):
                    decks[deck_name] = Deck(deck_name, questions)
            else:
                print("Deck name cannot be empty.")
    except RuntimeError as error:
        print("\nOnline quiz unavailable:", error)
        print("Switching to your local quiz decks.")
        if decks:
            print("\nAvailable Local Decks:")
            deck_names = list(decks.keys())
            for index, name in enumerate(deck_names, start=1):
                print(f"{index}. {name}")
            try:
                choice = int(input("Choose a local deck: "))
                if 1 <= choice <= len(deck_names):
                    selected_deck = decks[deck_names[choice - 1]]
                    play_deck(player_name, selected_deck)
                else:
                    print("Invalid deck choice.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("No local decks are available.")
def main():
    """Display the main menu and run QuizCraft."""
    print("================================")
    print("       QUIZCRAFT")
    print("================================")
    player_name = input("\nEnter your name: ").strip()
    if not player_name:
        print("Player name cannot be empty.")
        return
    try:
        decks = load_decks()
    except (FileNotFoundError, json.JSONDecodeError, KeyError) as error:
        print("Unable to load quiz decks:", error)
        return
    while True:
        print("\n========== MAIN MENU ==========")
        print("1. Play Local Quiz")
        print("2. Online Quiz")
        print("3. View Statistics")
        print("4. Exit")
        choice = input("\nEnter your choice: ").strip()
        if choice == "1":
            print("\nAvailable Decks:")
            deck_names = list(decks.keys())
            for index, name in enumerate(deck_names, start=1):
                print(f"{index}. {name}")
            try:
                deck_choice = int(input("Choose a deck: "))
                if 1 <= deck_choice <= len(deck_names):
                    selected_deck = decks[deck_names[deck_choice - 1]]
                    play_deck(player_name, selected_deck)
                else:
                    print("Invalid deck choice.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "2":
            online_quiz(player_name, decks)
        elif choice == "3":
            show_stats(player_name)
        elif choice == "4":
            print("\nThank you for using QuizCraft!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()