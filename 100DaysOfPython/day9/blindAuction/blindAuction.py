# from replit import clear
import art


# HINT: You can call clear() to clear the output in the console.
def blind_auction():
    print(art.logo)
    run_program = True
    print("Welcome to the secret auction program.")
    d = {}
    while run_program:
        name = input("What is your name?: ")
        bid = int(input("What's your bid?: $"))
        other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ")

        d[name] = bid
        # print(f"{other_bidders}")
        # print(d)
        if other_bidders == "no":
            run_program = False
            # print(d)
            print(f"The winner is {max(d, key=d.get)} with a bid of ${max(d.values())}")
            break


blind_auction()
