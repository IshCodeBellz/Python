from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while_on = True
while while_on:
    available_items = menu.get_items()
    order_name = input(f"What would you like? ({available_items}): ")
    if order_name == "off":
        while_on = False
    elif order_name == "report":
        print(coffee_maker.report(), money_machine.report())
    else:
        selected_drink = menu.find_drink(order_name)
        is_there_enough_resources = coffee_maker.is_resource_sufficient(selected_drink)
        if is_there_enough_resources:
            if money_machine.make_payment(selected_drink.cost):
                coffee_maker.make_coffee(selected_drink)