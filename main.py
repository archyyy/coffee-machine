from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_on = True
while machine_on :
    menuItems = menu.get_items()
    userInput = input(f'\nWhat would you like? ({menuItems}): ')
    if userInput == 'off' :
        machine_on = False
    elif userInput == 'report' :
        coffee_maker.report()
        money_machine.report()
    else :
        userDrink = menu.find_drink(userInput)
        if userDrink != None :
            is_resource_enought = coffee_maker.is_resource_sufficient(userDrink)
            is_payment_okay = money_machine.make_payment(userDrink.cost)
            if is_resource_enought and is_payment_okay :
                coffee_maker.make_coffee(userDrink)