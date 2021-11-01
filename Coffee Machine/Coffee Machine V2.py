class CoffeeMachine:
    def __init__(self):
        # Store details of different types of coffee
        self.espresso_info = {"name": "espresso", "water": 250, "milk": 0, "coffee beans": 16, "money": 4}
        self.latte_info = {"name": "latte", "water": 350, "milk": 75, "coffee beans": 20, "money": 7}
        self.cappuccino_info = {"name": "cappuccino", "water": 200, "milk": 100, "coffee beans": 12, "money": 6}
        self.coffee_infos = [self.espresso_info, self.latte_info, self.cappuccino_info]
        # Set initial stock
        self.stock = {"water": 400, "milk": 540, "coffee beans": 120, "disposable cups": 9, "money": 550}

    def print_state(self):
        # Print info of machine
        print()
        print("The coffee machine has:")
        print(self.stock["water"], "of water")
        print(self.stock["milk"], "of milk")
        print(self.stock["coffee beans"], "of coffee beans")
        print(self.stock["disposable cups"], "of disposable cups")
        print(self.stock["money"], "of money")
        print()

    def check_stock(self, coffee):
        for item in self.stock.keys():
            if item == "money":
                continue
            if item == "disposable cups":
                if self.stock[item] < 1:
                    return item
                continue
            if self.stock[item] < coffee[item]:
                return item
        return ""

    def confirm_order(self, coffee):
        for item in self.stock.keys():
            if item == "disposable cups":
                self.stock[item] -= 1
            elif item == "money":
                self.stock[item] += coffee[item]
            else:
                self.stock[item] -= coffee[item]

    def buy_coffee(self, choice):
        coffee = self.coffee_infos[choice - 1]
        # Check stock
        insufficient_item = self.check_stock(coffee)
        if insufficient_item:
            print("Sorry, not enough" + insufficient_item + "!")
            return
        else:
            print("I have enough resources, making you a coffee!")
            self.confirm_order(coffee)
            print()

    def refill_stock(self, new_items):
        self.stock["water"] += new_items[0]
        self.stock["milk"] += new_items[1]
        self.stock["coffee beans"] += new_items[2]
        self.stock["disposable cups"] += new_items[3]

    def take_money(self):
        # Give all money
        print("I gave you $" + str(self.stock["money"]))
        self.stock["money"] = 0
        print()

    def process_action(self, action, argument=None):
        if action == 'buy':
            self.buy_coffee(argument)
        elif action == 'fill':
            self.refill_stock(argument)
        elif action == 'take':
            self.take_money()
        else:
            self.print_state()


def main():
    coffee_machine = CoffeeMachine()

    while True:
        # Ask and process specified option
        print("Write action (buy, fill, take, remaining, exit):")
        action = input()
        if action == "exit":
            break

        elif action == "buy":
            # Ask user for choice of coffee
            print()
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
            choice = input()

            # Return to main menu if choice is back
            if choice == "back":
                print()
                pass
            else:
                choice = int(choice)
                coffee_machine.process_action('buy', choice)

        elif action == "fill":
            # Ask for qty of items to add
            print()
            print("Write how many ml of water you want to add:")
            water = int(input())
            print("Write how many ml of milk you want to add:")
            milk = int(input())
            print("Write how many grams of coffee beans you want to add:")
            coffee_beans = int(input())
            print("Write how many disposable coffee cups you want to add:")
            disposable_cups = int(input())
            print()

            coffee_machine.process_action('fill', [water, milk, coffee_beans, disposable_cups])

        elif action == "take":
            coffee_machine.process_action('take')

        else:
            coffee_machine.process_action('remaining')


main()
