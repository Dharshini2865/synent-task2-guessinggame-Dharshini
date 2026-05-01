# Task 2: Number Guessing Game
# Synent Technologies Python Internship
# Features: difficulty levels, hints, attempt counter, high score

import random
from colorama import init, Fore, Style
init(autoreset=True)


def show_banner():
    print(Fore.CYAN + "=" * 50)
    print(Fore.CYAN + "    NUMBER GUESSING GAME — Synent Internship")
    print(Fore.CYAN + "=" * 50)


def choose_difficulty():
    """Let the player choose a difficulty level"""
    print(Fore.WHITE + "\nChoose difficulty:")
    print(Fore.GREEN  + "  1. Easy   — Guess 1 to 50   (10 attempts)")
    print(Fore.YELLOW + "  2. Medium — Guess 1 to 100  (7 attempts)")
    print(Fore.RED    + "  3. Hard   — Guess 1 to 200  (5 attempts)")
    print()

    while True:
        choice = input(Fore.YELLOW + "Enter difficulty (1/2/3): ").strip()
        if choice == "1":
            return 50, 10, "Easy"
        elif choice == "2":
            return 100, 7, "Medium"
        elif choice == "3":
            return 200, 5, "Hard"
        else:
            print(Fore.RED + "  Please enter 1, 2, or 3.")


def get_hint(guess, secret, attempts_left):
    """Returns a helpful hint based on how close the guess is"""
    diff = abs(guess - secret)

    # Direction hint
    if guess < secret:
        direction = Fore.RED + "Too low!"
    else:
        direction = Fore.RED + "Too high!"

    # Warmth hint
    if diff <= 5:
        warmth = Fore.YELLOW + " Very warm!"
    elif diff <= 15:
        warmth = Fore.YELLOW + " Getting warmer..."
    elif diff <= 30:
        warmth = Fore.CYAN   + " Cold..."
    else:
        warmth = Fore.CYAN   + " Freezing!"

    attempts_msg = Fore.WHITE + f" ({attempts_left} attempts left)"
    return direction + warmth + attempts_msg


def play_round(high_score):
    """One full game round"""
    max_num, max_attempts, level = choose_difficulty()
    secret = random.randint(1, max_num)
    attempts = 0

    print(Fore.CYAN + f"\n  I'm thinking of a number between 1 and {max_num}.")
    print(Fore.CYAN + f"  You have {max_attempts} attempts. Good luck!\n")
    print(Fore.CYAN + "-" * 50)

    while attempts < max_attempts:
        # Get a valid guess from the player
        while True:
            try:
                raw = input(Fore.YELLOW + f"\nAttempt {attempts + 1}/{max_attempts} — Your guess: ")
                guess = int(raw)
                if 1 <= guess <= max_num:
                    break
                else:
                    print(Fore.RED + f"  Enter a number between 1 and {max_num}.")
            except ValueError:
                print(Fore.RED + "  Please enter a whole number!")

        attempts += 1
        attempts_left = max_attempts - attempts

        if guess == secret:
            score = max(0, (max_attempts - attempts + 1) * 10)
            print(Fore.GREEN + Style.BRIGHT + f"\n  Correct! The number was {secret}.")
            print(Fore.GREEN + f"  You got it in {attempts} attempt(s)!")
            print(Fore.GREEN + f"  Score: {score} points")
            if score > high_score:
                high_score = score
                print(Fore.YELLOW + "  New high score!")
            return True, high_score
        else:
            hint = get_hint(guess, secret, attempts_left)
            print("  " + hint)

            if attempts == max_attempts:
                print(Fore.RED + f"\n  Game over! The number was {secret}.")
                return False, high_score

    return False, high_score


def main():
    show_banner()
    high_score = 0
    games_played = 0
    wins = 0

    while True:
        print(Fore.CYAN + f"\n  High score: {high_score}  |  Wins: {wins}/{games_played}")
        print(Fore.WHITE + "\nMain menu:")
        print(Fore.GREEN + "  1. Play")
        print(Fore.RED   + "  2. Quit")
        print()

        choice = input(Fore.YELLOW + "Enter choice (1/2): ").strip()

        if choice == "2":
            print(Fore.CYAN + f"\nThanks for playing! Final score: {high_score}")
            print(Fore.CYAN + f"Games played: {games_played} | Wins: {wins}")
            break
        elif choice == "1":
            won, high_score = play_round(high_score)
            games_played += 1
            if won:
                wins += 1
            print(Fore.CYAN + "-" * 50)
        else:
            print(Fore.RED + "Please enter 1 or 2.")


if __name__ == "__main__":
    main()