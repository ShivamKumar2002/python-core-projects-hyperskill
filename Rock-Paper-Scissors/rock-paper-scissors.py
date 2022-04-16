import random


options = ["rock", "paper", "scissors"]

name = input("Enter your name: ")
print("Hello,", name)

user_options = input()
if user_options:
    options = user_options.split(",")

print("Okay, let's start")

with open("rating.txt") as f:
    ratings_list = f.readlines()
ratings = dict()
for rating in ratings_list:
    rating = rating.split()
    ratings[rating[0]] = int(rating[1])

user_rating = 0
if name in ratings:
    user_rating = ratings[name]

while True:
    user_choice = input()
    if user_choice == "!exit":
        break
    if user_choice == "!rating":
        print(user_rating)
        continue
    if user_choice not in options:
        print("Invalid input")
        continue
    computer_choice = random.choice(options)
    
    choice_index = options.index(computer_choice)
    remaining_options = options[choice_index + 1:] + options[:choice_index]
    winning_options = remaining_options[:len(remaining_options) // 2]

    if user_choice == computer_choice:
        print(f"There is a draw ({user_choice})")
        user_rating += 50
    elif user_choice in winning_options:
        print(f"Well done. The computer chose {computer_choice} and failed")
        user_rating += 100
    else:
        print(f"Sorry, but the computer chose {computer_choice}")

print("Bye!")
