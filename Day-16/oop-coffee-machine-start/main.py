from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


#Benefits of OOP

maker = CoffeeMaker()
dispenser = MoneyMachine()
display = Menu()

def coffee():

    x = input("You approach a coffee machine.):")
    if x == "off":
        print("goodbye")
        exit()
    
    elif x == "on":
        while True:
            options = display.get_items()
            choice = input(f"what would you like to drink?\nHere are the options: {options}")
            if choice == "report":
                maker.report()
                dispenser.report()
                return
            else:
                drink = display.find_drink(choice)
                if maker.is_resource_sufficient(drink) and dispenser.make_payment(drink.cost):
                    maker.make_coffee(drink)




coffee()






# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }

# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
#     "money": 0
# }
# def coins():
#     quarters = int(input("How many Quarters: ")) * .25
#     dimes = int(input("How many dimes: ")) * .10
#     nickles = int(input("How many nickles: ")) * .05
#     pennies = int(input("How many pennies: "))*.01

#     return quarters + dimes + nickles + pennies


# def process(key):

#     if resources["water"] - MENU[key]["ingredients"]["water"] < 0:
#         print("Sorry there is not enough water.")
#         return 0
#     if resources["milk"] - MENU[key]["ingredients"]["milk"] < 0:
#         print("Sorry there is not enough milk.")
#         return 0
#     if resources["coffee"] - MENU[key]["ingredients"]["coffee"]<0:
#         print("Sorry there is not enough coffee.")
#         return 0

#     resources["water"] -= MENU[key]["ingredients"]["water"]
#     resources["milk"] -= MENU[key]["ingredients"]["milk"]
#     resources["coffee"] -= MENU[key]["ingredients"]["coffee"]
#     resources["money"] += MENU[key]["cost"]
#     resources["money"] = round(resources["money"],2)
# def select():
#     global resources
#     x = input("What would you like? (report/espresso/latte/cappuccino):")
#     if x == "off":
#         print("goodbye")
#         exit()
#     if x == "report":
#         for x in resources:
#             print(f"{x} {resources[x]}")
#     elif x == "espresso":
#          change = round(coins() - MENU[x]["cost"],2)
#          if change <0:
#              print("Sorry that's not enough money. Money refunded. ")
#          elif change == 0:
#              if process(x) == 0:
#                  return
#              print("Thank you\nHere is your espresso. Enjoy!")
#          else:
#              if process(x) == 0:
#                  return
#              print(f"Here is your {change} in change and here is your espresso. Enjoy!")

#     elif x == "latte":
#         change = round(coins() - MENU[x]["cost"],2)
#         if change < 0:
#             print("Sorry that's not enough money. Money refunded. ")
#         elif change == 0:
#             if process(x) == 0:
#                 return
#             print("Thank you\nHere is your latte. Enjoy!")

#         else:
#             if process(x) == 0:
#                 return
#             print(f"Here is your {change} in change and here is your latte. Enjoy!")

#     elif x == "cappuccino":
#         change = round(coins() - MENU[x]["cost"],2)
#         if change < 0:
#             print("Sorry that's not enough money. Money refunded. ")
#         elif change == 0:
#             if process(x) == 0:
#                 return
#             print("Thank you\nHere is your cappuccino. Enjoy!")

#         else:
#             if process(x) == 0:
#                 return
#             print(f"Here is your {change} in change and here is your cappucinno. Enjoy!")






# if input("You find yourself at a Coffee Machine. Do you turn it on?").lower() == "y":
#     while True:
#         select()
#





