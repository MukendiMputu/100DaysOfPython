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
}

money = {
    "notes": 50,
    "coins": {
        "penny": 0.01,
        "nickel": 0.05,
        "dime": 0.1,
        "quarter": 0.25,
    }
}

running = True
gain = 0.0


def run():
    global running
    while running:
        choice = input("What would you like? (expresso - $1.59/cappuccino - $3/latte - $2.50): ")
        match choice:
            case 'off':
                running = False
            case 'report':
                print_report()
            case _:
                try:
                    drink = MENU[choice]
                    if are_sufficient_resources(drink):
                        payment = process_money()
                        if is_transaction_successful(payment, drink['cost']):
                            make_coffee(choice)
                except KeyError:
                    print("Invalid choice.")


def print_report():
    print(
        f"There is:\n\t{resources['water']}ml of water\n\t{resources['milk']}ml of milk\n\t{resources['coffee']}g of coffee"
    )
    print(f"\tand ${money['coins']['penny']+money['coins']['dime']+money['coins']['quarter']+money['notes']}")


def are_sufficient_resources(drink):
    """Returns True when there are enough resources"""
    for ingredient in drink['ingredients']:
        if drink['ingredients'][ingredient] >= resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
        return True


def process_money():
    print("Please insert coins.")
    try:
        total = int(input("How many penny's? ")) * 0.01
        total += int(input("How many nickels? ")) * 0.05
        total += int(input("How many dimes? ")) * 0.1
        total += int(input("How many quarters? ")) * 0.25
        total += int(input("How many dollars? ")) * 1.0
    except ValueError:
        print("Invalid coins or notes.")
    return total


def is_transaction_successful(in_money, drink_cost):
    if in_money >= drink_cost:
        change = round(in_money - drink_cost, 2)
        print(f"Here is your ${change} in change.")
        global gain
        gain += drink_cost
        return True
    else:
        print(f"Sorry ${in_money} is not enough money. Money refunded.")
        return False


def make_coffee(drink):
    # TODO: adjust resource amount and gain
    print(f"Here is your {drink} ☺")
    print(f"Here is your {drink}")


if __name__ == '__main__':
    run()
