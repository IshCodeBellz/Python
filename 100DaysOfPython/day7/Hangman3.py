# Step 3

import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

# TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

chosen_word_list = []
chosen_word_list[:0] = chosen_word

while chosen_word_list != display:
    guess = input("Guess a letter: ").lower()

    count = -1
    for letter in chosen_word:
        count = count + 1
        if letter == guess:
            for letter in display:
                display[count] = guess
        else:
            continue
    print(display)
if chosen_word_list == display:
    print("You win.")