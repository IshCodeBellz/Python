import art
import random


# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


def random_num():
    random_number = random.randint(1, 101)
    return random_number


def level():
    choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if choice == "easy":
        game_level = 10
        return game_level
    elif choice == "hard":
        game_level = 5
        return game_level
    else:
        print("Incorrect input, please try again")


def game_guess():
    count = choice
    for numbers in range(count):
        guess = int(input("Make a guess: "))
        if guess == random_number:
            print(f"You got it! The answer was {guess}.")
            return 0
        else:
            count -= 1
            if guess < random_number:
                print("Too Low")
                print("Guess again.")
                print(f"You have {count} attempts remaining to guess the number.")
            elif guess > random_number:
                print("Too High")
                print("Guess again.")
                print(f"You have {count} attempts remaining to guess the number.")

    if count == 0:
        print("You've run out of guesses, you lose.")
        return 0


print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
random_number = random_num()
print(f"Pssst, the correct answer is {random_number}")
choice = level()
print(f"You have {choice} attempts remaining to guess the number.")
guess = game_guess()
