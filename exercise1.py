import random
from typing import Tuple

def get_answer() -> int:
    return random.randint(0, 100)

def check(guess: int, target: int) -> Tuple[bool, str]:

    if guess > target:
        response = (True, "Too high!")
    elif guess < target:
        response = (True, "Too low!")
    else:
        response = (False, "Just right!")
    return response


def guessing_game():
    answer = get_answer()
    print("Welcome to Guess the Number!")
    guessed_wrong = True

    while guessed_wrong:
        try:
            user_input = input('Enter your guess: ')
            guess = int(user_input)
            (guessed_wrong, message) = check(guess, answer)
            print(message)
        except ValueError:
            print(f" {user_input} is not an integer.")


if __name__ == "__main__":
    guessing_game()