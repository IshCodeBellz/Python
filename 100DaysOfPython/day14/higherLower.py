import art
import game_data
import random
# from replit import clear


def format_data(account):
    """ Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc} from {account_country}"


def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and return if they got it right"""
    if a_follower_count > b_follower_count:
        return guess == "A"
    else:
        return guess == "B"


# display art
print(art.logo)
score = 0
game_should_continue = True
account_B = random.choice(game_data.data)
# make the game repeatable
while game_should_continue:

    # generate a random account from the game data
    # making account at position B become the next account at position A.
    account_A = account_B
    account_B = random.choice(game_data.data)

    while account_A == account_B:
        account_B = random.choice(game_data.data)

    print(f"Compare A: {format_data(account_A)}.")
    print(art.vs)
    print(f"Against B: {format_data(account_B)}.")

    # ask user for a guess

    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    # check if user is correct
    ## get follower count of each account
    a_follower_count = account_A["follower_count"]
    b_follower_count = account_B["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # clear the screen between rounds
    # clear()
    # print(art.logo)

    # give user feedback on their guess
    # score keeping
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}.")

#
#