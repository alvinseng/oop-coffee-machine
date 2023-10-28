from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
report = CoffeeMaker()
money = MoneyMachine()

# print(item)


is_on = True
items_on_menu = menu.get_items()
print(f"Menu of the day:\n{items_on_menu}\n")  # prints the items on the menu

while is_on:
    phrases_to_exclude = ["menu", "report"]

    coffeeOrder = input("What would you like to order today?\n").lower()
    # coffeeOrder = "cappuccino" # Testing code with set drink

    # List of phrases that should not trigger the "Sorry" message
    if coffeeOrder not in phrases_to_exclude:
        ordered_item = menu.find_drink(coffeeOrder)
        if ordered_item is not None:
            cost_of_item = '${:,.2f}'.format(ordered_item.cost)
            print(f"The cost of {coffeeOrder} is {cost_of_item}")
    elif coffeeOrder == "menu":
        print(f"Menu of the day:\n{items_on_menu}\n")
    elif coffeeOrder == "report":
        report.report()
        money.report()
        is_on = False
    else:
        is_on = False

