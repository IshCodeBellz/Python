MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def insert_coin():
    print("Please insert coins.")
    total = int(input("how many quarters?:")) * 0.25
    total += int(input("how many dimes?:")) * 0.1
    total += int(input("how many nickles?:")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def resources_check(drink):
    if coins > MENU[drink]["cost"]:
        if drink == "espresso" and resources["water"] >= MENU[drink]["ingredients"]["water"] and resources["coffee"] >= \
                MENU[drink]["ingredients"]["coffee"]:
            new_water = resources["water"] - MENU[drink]["ingredients"]["water"]
            resources["water"] = new_water
            new_coffee = resources["coffee"] - MENU[drink]["ingredients"]["coffee"]
            resources["coffee"] = new_coffee
            change = coins - MENU[drink]["cost"]
            new_money = resources["money"] + MENU[drink]["cost"]
            resources["money"] = new_money
            print(f"Here is ${change} in change.")
            print(f"Here is your {drink} ☕️. Enjoy!")
        elif resources["water"] >= MENU[drink]["ingredients"]["water"] and resources["coffee"] >= \
                MENU[drink]["ingredients"]["coffee"] and resources["milk"] >= MENU[drink]["ingredients"]["milk"]:
            new_water = resources["water"] - MENU[drink]["ingredients"]["water"]
            resources["water"] = new_water
            new_coffee = resources["coffee"] - MENU[drink]["ingredients"]["coffee"]
            resources["coffee"] = new_coffee
            new_milk = resources["milk"] - MENU[drink]["ingredients"]["milk"]
            resources["milk"] = new_milk
            change = coins - MENU[drink]["cost"]
            new_money = resources["money"] + MENU[drink]["cost"]
            resources["money"] = new_money
            print(f"Here is ${change} in change.")
            print(f"Here is your {drink} ☕️. Enjoy!")
        else:
            print("Sorry, There is not enough resources for your drink.")
    else:
        print("Sorry that's not enough money. Money refunded.")


def print_report():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = resources["money"]
    return f"Water: {water}ml \nMilk: {milk}ml \nCoffee: {coffee}g \nMoney: ${money}"


# print(MENU["espresso"]["ingredients"]["water"])

askUser = True
while askUser:
    userInp = input("What would you like? (espresso/latte/cappuccino):").lower()
    if userInp == "off":
        askUser = False
    elif userInp == "latte":
        coins = insert_coin()
        print(coins)
        resources_check("latte")
        continue
    elif userInp == "cappuccino":
        coins = insert_coin()
        print(coins)
        resources_check("cappuccino")
        continue
    elif userInp == "espresso":
        coins = insert_coin()
        print(coins)
        resources_check("espresso")
    elif userInp == "report":
        print(print_report())

