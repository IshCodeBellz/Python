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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def insert_coin():
    """Returns the total calculated from inserted coins"""
    print("Please insert coins.")
    total = int(input("how many quarters?:")) * 0.25
    total += int(input("how many dimes?:")) * 0.1
    total += int(input("how many nickles?:")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted or False if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded. ")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️")


def print_report():
    """Returns report of resources"""
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    return f"Water: {water}ml \nMilk: {milk}ml \nCoffee: {coffee}g \nMoney: ${profit}"


def enough_resources(ingredients):
    """Returns True if order can be made and False if resources aren't enough"""
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"sorry there is not enough {item}")
            return False
    return True


askUser = True
while askUser:
    userInp = input("What would you like? (espresso/latte/cappuccino):").lower()
    if userInp == "off":
        askUser = False
    elif userInp == "report":
        print(print_report())
    else:
        drink = MENU[userInp]
        if enough_resources(drink["ingredients"]):
            payment = insert_coin()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(userInp,drink["ingredients"])
