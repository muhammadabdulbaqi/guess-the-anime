# import requests
# import random

# # Step 1: Get top anime list
# response = requests.get("https://api.jikan.moe/v4/top/anime")
# data = response.json()

# anime_list = data['data']  # List of top anime
# anime_ids = [anime['mal_id'] for anime in anime_list]
# anime_titles = [anime['title'] for anime in anime_list]  # Store titles for distractors

# # Step 2: Pick a random anime
# correct_anime_id = random.choice(anime_ids)

# # Step 3: Fetch full details of selected anime
# anime_details = requests.get(f"https://api.jikan.moe/v4/anime/{correct_anime_id}/full").json()
# synopsis = anime_details['data']['synopsis']
# correct_title = anime_details['data']['title']

# # Step 4: Get 2 distractor titles (excluding correct one)
# distractors = random.sample([title for title in anime_titles if title != correct_title], 2)

# # Final question data
# question = {
#     "synopsis": synopsis,
#     "options": [correct_title] + distractors
# }
# random.shuffle(question["options"])  # Shuffle options

# # Print output
# print(question)

# main.py
import random
import requests
from test_anime_fetch import fetch_top_anime

def create_question():
    """
    Creates a quiz question using anime data.
    :return: A dictionary containing the question and options
    """
    # Step 1: Fetch anime data
    all_anime = fetch_top_anime(max_pages=3)

    # Extract anime IDs and titles
    anime_ids = [anime['mal_id'] for anime in all_anime]
    anime_titles = [anime['title'] for anime in all_anime]  # Store titles for distractors

    # Step 2: Pick a random anime
    correct_anime_id = random.choice(anime_ids)

    # Step 3: Fetch full details of selected anime
    anime_details = requests.get(f"https://api.jikan.moe/v4/anime/{correct_anime_id}/full").json()
    synopsis = anime_details['data']['synopsis']
    correct_title = anime_details['data']['title']

    # Step 4: Get 2 distractor titles (excluding correct one)
    distractors = random.sample([title for title in anime_titles if title != correct_title], 2)

    # Final question data
    question = {
        "synopsis": synopsis,
        "options": [correct_title] + distractors
    }
    random.shuffle(question["options"])  # Shuffle options to randomize the order

    return question

# Main function to run the game
if __name__ == "__main__":
    question = create_question()
    print(question)
