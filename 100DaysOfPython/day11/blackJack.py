import random
import click
# from replit import clear
import art


def clrscr():
    # Clear screen using click.clear() function
    click.clear()


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_number = random.randint(0, 12)
    random_card = cards[random_number]
    return random_card


def calculate_score(list_of_cards):
    list_of_cards_total = 0
    for numbers in list_of_cards:
        list_of_cards_total += numbers
    if 10 in list_of_cards and 11 in list_of_cards:
        return 0
    elif 11 in list_of_cards:
        if list_of_cards_total > 21:
            list_of_cards.remove(11)
            list_of_cards.append(1)
            return list_of_cards_total
        else:
            return list_of_cards_total
    else:
        return list_of_cards_total


def compare(user, computer):
    if user == computer:
        return "It's a Draw 😒😒"
    elif computer == 0:
        return "You Lose! Computer has a BlackJack 🃏👎🏾"
    elif user == 0:
        return "You Win !!! BlackJack 😎🕺🏾"
    elif user > 21:
        return "You Lose! You Went over 🤬😢"
    elif computer > 21:
        return "You Win !!! Computer went over 💩😜"
    elif user > computer:
        return "You Win !!! BlackJack 😎🕺🏾🤩"
    else:
        return "You Lose! 🃏👎🏾🤬"


def play_game():
    print(art.logo)
    user_cards = []
    computer_cards = []
    game = True

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while game:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {computer_cards[0]}")

        if computer_score == 0 or user_score == 0:
            game = False
        else:
            draw_card = input("Would you like to draw another card? Y or N: ").capitalize()
            if draw_card == "Y":
                user_cards.append(deal_card())
                calculate_score(user_cards)
            elif draw_card == "N":
                game = False

    while calculate_score(computer_cards) != 0 and calculate_score(computer_cards) < 17:
        computer_cards.append(deal_card())
        calculate_score(computer_cards)

    final_computer_score = calculate_score(computer_cards)
    final_user_score = calculate_score(user_cards)
    print(f"    Your final hand: {user_cards}, final score: {final_user_score}")
    print(f"    Computers final hand: {computer_cards}, final score: {final_computer_score}")
    print(compare(final_user_score, final_computer_score))


while input("Do you want to play again? Type 'Y' or 'N': ").capitalize() == "Y":
    clrscr()
    # clear()
    play_game()
