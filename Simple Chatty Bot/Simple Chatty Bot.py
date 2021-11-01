# Greet the user
print("Hello! My name is ChattyBot.")
print("I was created in 2021.")

# Get name of user
print("Please, remind me your name.")
user_name = input()
print("What a great name you have, " + user_name + "!")

# Guess age of user
print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")
remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print("Your age is " + str(age) + "; that's a good time to start programming!")

# Count
print("Now I will prove to you that I can count to any number you want.")
end_num = int(input())
for i in range(end_num+1):
    print(i, "!")

# Simple quiz
print("Let's test your programming knowledge.")
print("Which of following is four?")
print("1. I")
print("2. II")
print("3. III")
print("4. IV")

while True:
    answer = int(input())
    if answer == 4:
        break
    else:
        print("Please, try again.")

print("Completed, have a nice day!")
print("Congratulations, have a nice day!")
