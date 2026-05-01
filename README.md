# synent-task2-guessinggame-Dharshini
# 🎮 Number Guessing Game

A fun number guessing game with difficulty levels, smart hints, and a scoring system.

## Features
- 3 difficulty levels — Easy (1–50), Medium (1–100), Hard (1–200)
- Warmth-based hints — "Very warm!", "Getting warmer...", "Cold...", "Freezing!"
- Attempt counter per round
- Score system — fewer attempts = higher score
- High score tracker across multiple rounds
- Win/loss record display

## Requirements
```bash
pip install colorama
```

## How to Run
```bash
python guessing_game.py
```

## How to Use
1. Run the program
2. Select Play from the main menu
3. Choose a difficulty level
4. Enter your guesses — use the hints to close in
5. Try to guess the number in as few attempts as possible!

## Difficulty Levels
| Level  | Range   | Attempts |
|--------|---------|----------|
| Easy   | 1–50    | 10       |
| Medium | 1–100   | 7        |
| Hard   | 1–200   | 5        |

## Technologies Used
- Python 3
- `random` — secret number generation
- `colorama` — colored terminal output
