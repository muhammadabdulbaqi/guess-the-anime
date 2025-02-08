from flask import Flask, jsonify, request
import random
import uuid
from game_logic import create_question
from test_anime_fetch import fetch_top_anime

app = Flask(__name__)

# Temporary storage for game sessions
games = {}

@app.route('/')
def home():
    return "Welcome to Guess the Anime API!"

@app.route('/question', methods=['GET'])
def get_question():
    """Starts a new game and returns the first question."""
    game_id = str(uuid.uuid4())
    all_anime = fetch_top_anime(max_pages=3)
    question = create_question(all_anime)
    
    games[game_id] = {
        "score": 0,
        "all_anime": all_anime,
        "current_question": question
    }
    
    return jsonify({"game_id": game_id, "question": question})

@app.route('/game/answer', methods=['POST'])
def submit_answer():
    """Handles user answer submission and returns the next question or game over."""
    data = request.json
    game_id = data.get("game_id")
    user_answer = data.get("user_answer")

    if game_id not in games:
        return jsonify({"error": "Invalid game_id"}), 400
    
    game = games[game_id]
    correct_answer = game["current_question"]["correct_answer"]
    
    if user_answer == correct_answer:
        game["score"] += 1
        game["current_question"] = create_question(game["all_anime"])
        return jsonify({
            "correct": True,
            "score": game["score"],
            "next_question": game["current_question"]
        })
    else:
        final_score = game["score"]
        del games[game_id]  # Remove game session
        return jsonify({
            "correct": False,
            "final_score": final_score,
            "message": "Game Over!"
        })

if __name__ == '__main__':
    app.run(debug=True)
