import json
from models import Deck, QuizSession
from storage import save_progress, get_player_progress
def load_decks():
    """Load all quiz decks from the JSON file."""
    with open("decks.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    decks = {}
    for deck_name, deck_data in data.items():
        decks[deck_name] = Deck(deck_name, deck_data["questions"])

    return decks
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
def main():
    """Display the main menu and run QuizCraft."""
    print("================================")
    print("       QUIZCRAFT")
    print("================================")
    player_name = input("\nEnter your name: ").strip()
    if not player_name:
        print("Player name cannot be empty.")
        return
    decks = load_decks()
    while True:
        print("\n========== MAIN MENU ==========")
        print("1. Play Quiz")
        print("2. View Statistics")
        print("3. Exit")
        choice = input("\nEnter your choice: ").strip()
        if choice == "1":
            print("\nAvailable Decks:")
            deck_names = list(decks.keys())
            for index, name in enumerate(deck_names, start=1):
                print(f"{index}. {name}")
            try:
                deck_choice = int(input("Choose a deck: "))
                if 1 <= deck_choice <= len(deck_names):
                    selected_name = deck_names[deck_choice - 1]
                    selected_deck = decks[selected_name]
                    session = QuizSession(player_name, selected_deck)
                    result = session.run()
                    save_progress(player_name, result)
                    print("\nYour progress has been saved!")
                else:
                    print("Invalid deck choice.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "2":
            show_stats(player_name)
        elif choice == "3":
            print("\nThank you for using QuizCraft!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()