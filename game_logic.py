import random
import requests
from test_anime_fetch import fetch_top_anime

def fetch_anime_details(anime_id):
    """
    Fetches full details for a specific anime.
    :param anime_id: The MyAnimeList ID of the anime
    :return: A dictionary containing title and synopsis
    """
    anime_details = requests.get(f"https://api.jikan.moe/v4/anime/{anime_id}/full").json()
    return {
        "title": anime_details['data']['title'],
        "synopsis": anime_details['data']['synopsis']
    }

def create_question(all_anime):
    """
    Creates a quiz question using anime data.
    :return: A dictionary containing the question and options
    """
    # Step 1: Pick a random anime
    correct_anime = random.choice(all_anime)

    # Fetch full details
    details = fetch_anime_details(correct_anime['mal_id'])
    correct_title = details["title"]
    synopsis = details["synopsis"]

    # Step 2: Get 2 distractor titles (excluding correct one)
    distractors = random.sample([anime['title'] for anime in all_anime if anime['title'] != correct_title], 2)

    # Final question data
    question = {
        "synopsis": synopsis,
        "options": [correct_title] + distractors,
        "correct_answer": correct_title  # Store correct answer separately
    }
    random.shuffle(question["options"])  # Shuffle options

    return question
