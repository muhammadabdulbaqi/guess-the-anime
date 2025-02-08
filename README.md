# Guess the Anime Game API

## Current Capabilities

- **API Setup**: The game is currently set up as a Flask API, allowing users to fetch quiz questions dynamically.
- **Get a Question**: The `/question` endpoint provides a quiz question in JSON format. The question includes:
  - A **synopsis** of the anime.
  - **Options** for the user to select from.
  - The **correct answer** for reference.

### Example Response:

```json
{
  "correct_answer": "Kingdom 3rd Season",
  "options": [
    "Kingdom 3rd Season",
    "Mo Dao Zu Shi: Wanjie Pian",
    "Tian Guan Cifu Er"
  ],
  "synopsis": "Following the successful Sanyou campaign, the Qin army, including 1,000-Man Commander Xin, inches ever closer to fulfilling King Ying Zheng's dream of unifying China..."
}
```
## Intended Next Steps

### 1. **Game Flow**:
   - Implement an endpoint to manage the full game flow (e.g., `/game`).
   - Enable users to start the game, answer questions, and receive feedback.
   - Track the player's score throughout the game and return it when the game ends.
   - Example: `POST /game` to submit answers and receive updated scores.

### 2. **Leaderboard**:
   - Introduce a leaderboard feature to track top scorers.
   - Save user scores in a database (e.g., SQLite or PostgreSQL).
   - Create an endpoint to fetch the leaderboard data, showing the top scores.

### 3. **Frontend Development**:
   - Develop a React app to serve as the user interface.
   - Fetch quiz questions from the Flask API backend.
   - Display questions, options, and handle user interactions.
   - Allow users to submit answers and view their scores in real time.

### 4. **Database Integration**:
   - Store anime data (e.g., titles, synopses) in a database to minimize repeated API calls.
   - Save user game data, such as their score, answers, and game history.
   - Implement a database model to handle both anime data and user scores efficiently.
