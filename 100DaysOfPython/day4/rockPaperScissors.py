import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

print("Welcome to the rock paper scissors!")

selection = input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")
player_selection = int(selection)
print(player_selection)
computer_selection = random.randint(0, 2)
print(computer_selection)

if player_selection == 0:
    print(rock)
    if computer_selection == 0:
        print("its a Draw -_- ")
    elif computer_selection == 1:
        print("The Computer Wins, you lose ...")
    elif computer_selection == 2:
        print("You Win !!!")
elif player_selection == 1:
    print(paper)
    if computer_selection == 0:
        print("You Win !!!")
    elif computer_selection == 1:
        print("its a Draw -_- ")
    elif computer_selection == 2:
        print("The Computer Wins, you lose ...")
elif player_selection == 2:
    print(scissors)
    if computer_selection == 0:
        print("The Computer Wins, you lose ...")
    elif computer_selection == 1:
        print("You Win !!!")
    elif computer_selection == 2:
        print("its a Draw -_- ")


if computer_selection == 0:
    print(rock)
elif computer_selection == 1:
    print(paper)
elif computer_selection == 2:
    print(scissors)
