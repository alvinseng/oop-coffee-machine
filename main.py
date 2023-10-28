from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
report = CoffeeMaker()
money = MoneyMachine()

# print(item)
phrases_to_exclude = ["menu", "report"]
items_on_menu = menu.get_items()

def menu_items():
    # split string into individual menu item
    menu_items_list = items_on_menu.split('/')
    #process and print each menu item separately
    for item in menu_items_list:
        item_name = item.strip()
        ordered_item = menu.find_drink(item_name)
        if ordered_item is not None:
            cost_of_item = '${:,.2f}'.format(ordered_item.cost)
            print(f" {item_name}: {cost_of_item}")


is_on = True

while is_on:
    print("Menu:")
    menu_items()  # prints the items on the menu
    coffeeOrder = input("What would you like to order today?\n").lower()
    # coffeeOrder = "cappuccino" # Testing code with set drink

    # List of phrases that should not trigger the "Sorry" message
    if coffeeOrder not in phrases_to_exclude:
        ordered_item = menu.find_drink(coffeeOrder)
        if ordered_item is not None:
            global cost_of_item
            print(f"The cost of {coffeeOrder} is {cost_of_item}")
    # elif coffeeOrder == "menu":
    #     menu_items()
    elif coffeeOrder == "report":
        report.report()
        money.report()
        is_on = False
    else:
        is_on = False

