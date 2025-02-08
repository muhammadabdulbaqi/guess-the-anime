from flask import Flask, jsonify
from game_logic import create_question
from test_anime_fetch import fetch_top_anime

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Guess the Anime API!"

@app.route('/question', methods=['GET'])
def get_question():
    """
    API endpoint to serve a new quiz question.
    Fetches anime data, generates a question, and returns it as JSON.
    """
    all_anime = fetch_top_anime(max_pages=3)  # Fetch anime data
    question = create_question(all_anime)    # Create a quiz question
    return jsonify(question)  # Return question as JSON

if __name__ == "__main__":
    app.run(debug=True)
