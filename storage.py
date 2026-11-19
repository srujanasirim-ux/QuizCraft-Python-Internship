import json
import os
PROGRESS_FILE = "progress.json"
def load_progress():
    """Load saved player progress from the JSON file."""
    if not os.path.exists(PROGRESS_FILE):
        return {}
    try:
        with open(PROGRESS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return {}
def save_progress(player_name, result):
    """Save a player's quiz result in the JSON file."""
    progress = load_progress()
    if player_name not in progress:
        progress[player_name] = []
    progress[player_name].append(result)
    with open(PROGRESS_FILE, "w", encoding="utf-8") as file:
        json.dump(progress, file, indent=4)
def get_player_progress(player_name):
    """Return all quiz results belonging to a player."""
    progress = load_progress()
    return progress.get(player_name, [])