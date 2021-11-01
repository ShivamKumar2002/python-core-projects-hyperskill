def print_state(stock):
    print()
    print("The coffee machine has:")
    print(stock["water"], "of water")
    print(stock["milk"], "of milk")
    print(stock["coffee beans"], "of coffee beans")
    print(stock["disposable cups"], "of disposable cups")
    print(stock["money"], "of money")
    print()


def check_resources(coffee, stock):
    for item in stock.keys():
        if item == "money":
            continue
        if item == "disposable cups":
            if stock[item] < 1:
                return item
            continue
        if stock[item] < coffee[item]:
            return item
    return ""


def process_purchase(coffee, stock):
    print("I have enough resources, making you a coffee!")
    for item in stock.keys():
        if item == "disposable cups":
            stock[item] -= 1
        elif item == "money":
            stock[item] += coffee[item]
        else:
            stock[item] -= coffee[item]
    print()
    return stock


def process_buy(stock):
    # Store details of different types of coffee
    espresso_info = {"name": "espresso", "water": 250, "milk": 0, "coffee beans": 16, "money": 4}
    latte_info = {"name": "latte", "water": 350, "milk": 75, "coffee beans": 20, "money": 7}
    cappuccino_info = {"name": "cappuccino", "water": 200, "milk": 100, "coffee beans": 12, "money": 6}

    coffee_infos = [espresso_info, latte_info, cappuccino_info]

    # Ask user for choice of coffee
    print()
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    choice = input()

    # Return to main menu if choice is back
    if choice == "back":
        return stock

    choice = int(choice)
    coffee = coffee_infos[choice - 1]

    # Check Resources
    insufficient_item = check_resources(coffee, stock)

    if insufficient_item:
        print("Sorry, not enough" + insufficient_item + "!")

    else:
        # Process purchase if all resources available
        stock = process_purchase(coffee, stock)

    return stock


def process_fill(stock):
    # Ask for qty of items to add
    print("Write how many ml of water you want to add:")
    water = int(input())
    print("Write how many ml of milk you want to add:")
    milk = int(input())
    print("Write how many grams of coffee beans you want to add:")
    coffee_beans = int(input())
    print("Write how many disposable coffee cups you want to add:")
    disposable_cups = int(input())

    # Modify stock accordingly
    stock["water"] += water
    stock["milk"] += milk
    stock["coffee beans"] += coffee_beans
    stock["disposable cups"] += disposable_cups

    return stock


def process_take(stock):
    # Give all money
    print("I gave you $" + str(stock["money"]))
    stock["money"] = 0

    return stock


def main():
    # Initial stock
    stock = {"water": 400, "milk": 540, "coffee beans": 120, "disposable cups": 9, "money": 550}

    while True:
        # Ask and process specified option
        print("Write action (buy, fill, take, remaining, exit):")
        action = input()
        if action == "buy":
            # Buy a coffee
            stock = process_buy(stock)
        elif action == "fill":
            # Re-fill the machine
            stock = process_fill(stock)
        elif action == "take":
            # Take money
            stock = process_take(stock)
        elif action == "remaining":
            # Print stock
            print_state(stock)
        else:
            break


main()
