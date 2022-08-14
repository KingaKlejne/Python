# Menu dictionary
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


# TODO 1: Function for sum of total amount
def count_total_amount():
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))

    penny = 0.01
    nickel = 0.05
    dime = 0.1
    quarter = 0.25

    sum_quarters = quarters * quarter
    sum_dimes = dimes * dime
    sum_nickles = nickles * nickel
    sum_pennies = pennies * penny

    total = sum_quarters + sum_dimes + sum_nickles + sum_pennies
    return total


# TODO 2: Function to check if there is enough ingredients
def check_ingredients(ingredients, user_input, drink, check):
    for key in drink['ingredients']:
        if ingredients[key] < drink['ingredients'][key]:
            print(f"Sorry there is not enough {key}.")
            check = 0
            return check


# TODO 3: Function to check if there is enough money
def check_money(total, drink):
    if total < drink['cost']:
        print("Sorry that's not enough money. Money refunded.")
        rest = 0
        return rest
    else:
        rest = round(total - drink['cost'], 2)
        return rest


# TODO 4: Function to get ingridents from the machine
def get_ingredients(ingredients, user_input, drink, total, rest):
    for key in drink['ingredients']:
        ingredients[key] -= drink['ingredients'][key]

    ingredients["money"] += round(total - rest, 2)
    print(f"Here is ${change} in change.")
    print(f"Here is your {answer}. Enjoy!")
    return ingredients


# TODO 5: Function to show the report
def report():
    print(f" Water: {supplies['water']}ml \n "
          f"Milk: {supplies['milk']}ml \n "
          f"Coffee: {supplies['coffee']}g \n "
          f"Money: ${supplies['money']} ")

# TODO 6: Start Game
game = True
supplies = {"water": 300, "milk": 200, "coffee": 100, "money": 0}

while game:

    # Phase 1
    answer = input("\tWhat would you like? (espresso/latte/cappuccino): ")
    if answer != 'report' and answer in ('espresso', 'latte', 'cappuccino'):
        coffee = MENU[answer]
        stop_point = 100

        # Check if there are enough supplies
        stop_point = check_ingredients(supplies, answer, coffee, breakpoint)

        # Get money
        if stop_point != 0:
            total_sum = count_total_amount()

            # Check if there is enough money
            change = check_money(total_sum, coffee)

            if change != 0:
                # Get supplies and give coffee
                supplies = get_ingredients(supplies, answer, coffee, total_sum, change)

        # Finish
        else:
            game = False

    # Report
    elif answer == 'report':
        report()

    # Incorrect answer
    else:
        print("Wrong item selected. Please try again")
