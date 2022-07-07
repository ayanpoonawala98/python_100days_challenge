from time import sleep

from prompt_toolkit.shortcuts import clear

from recipe import MENU,profit,resources

def coffeeMaker(coffeeName):
    juice = MENU.get(coffeeName).get('ingredients')
    resources["water"] -= juice['water']
    resources["milk"] -= juice['milk']
    resources["coffee"] -= juice['coffee']
    global profit
    profit += MENU.get(coffeeName).get("cost")
    sleep(15)


def report():
    print( f"water:{resources.get('water')}\n" \
           f"Milk:{resources.get('milk')}\n" \
           f"Coffee:{resources.get('coffee')}\n "\
           f"Money:${profit}")
    machine()
def refill():
    water = input(f"How much water need to be add(ml):")
    resources["water"] += int(water)
    milk = input(f"How much milk need to be add(ml):")
    resources["milk"] += int(milk)
    coffee = input(f"How much coffee bean need to be add(grams):")
    resources["coffee"] += int(coffee)

    print("Resource add successfully...")
    report()

def checkResource(coffeeName):
    coffee=MENU.get(coffeeName).get('ingredients')
    return resources.get("water") > coffee["water"] and resources.get('milk') > coffee['milk'] and resources.get('coffee') > coffee["coffee"]

def calculateCost(quarters,dimes,nickles,pennies):
    total = quarters * 25 + dimes * 10 + nickles * 5 + pennies
    return round(total / 100, 2)

def checkAmount(coffeeName,totalAmount):
    coffee = MENU.get(coffeeName)
    return coffee['cost'] <= totalAmount

def addMoney(coffeeName):
    if(checkResource(coffeeName)):
        print('please insert coins.')
        quarters = int(input("How many Quarters?"))
        dimes = int(input("How many Dimes?"))
        nickles = int(input("How many Nickles?"))
        pennies = int(input("How many Pennies?"))

        total = calculateCost(quarters,dimes,nickles,pennies)
        if(checkAmount(coffeeName,total)):

            print(f'Here is ${total - MENU.get(coffeeName).get("cost")} in change.')
            coffeeMaker(coffeeName)
            print(f'Here is your {coffeeName}. Enjoy!')
            machine()
        else:
            print(f'Insufficient coin added,please add more coin or take different type of coffee.Thank you')
            machine()
    else:
        action = int(input(f'Resources are insufficient,\n 1.Refill. \n 2.Other Order \n Answer :--'))
        if(action == 1):
            refill()
        else:
            machine()





def machine():
    coffee = input("what would you like? (espresso/latte/cappuccino/report/refill/off):").lower()
    if coffee not in ["espresso", "latte", "cappuccino", "report", "refill","off"]:
        print(f"{coffee} is not type of coffee,please select right choice...")
        machine()

    if coffee == "off":
        exit()
    elif coffee == "report":
        report()
    elif coffee == "refill":
        refill()
    else:
        addMoney(coffee)



machine()
