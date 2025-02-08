from test_anime_fetch import fetch_top_anime
from game_logic import create_question

def play_game():
    """
    Runs the main game loop where the player keeps answering until they fail.
    """
    all_anime = fetch_top_anime(max_pages=3)  # Fetch anime data
    score = 0

    while True:
        question = create_question(all_anime)
        print("\nGuess the anime from this synopsis:\n")
        print(question["synopsis"])
        print("\nOptions:")
        
        for idx, option in enumerate(question["options"], 1):
            print(f"{idx}. {option}")

        # Get user input
        try:
            user_choice = int(input("\nEnter the number of your answer: "))
            if question["options"][user_choice - 1] == question["correct_answer"]:
                score += 1
                print("✅ Correct! Your score:", score)
            else:
                print(f"❌ Wrong! The correct answer was: {question['correct_answer']}")
                break  # End game on wrong answer

        except (ValueError, IndexError):
            print("Invalid input. Please enter a valid number.")

    print(f"\nGame Over! Your final score: {score}")

if __name__ == "__main__":
    play_game()
