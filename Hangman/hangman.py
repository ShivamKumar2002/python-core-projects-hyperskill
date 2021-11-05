import random


def main():
    words = ['python', 'java', 'kotlin', 'javascript']
    correct_word = random.choice(words)  # Randomly choose a word
    remaining_set = set(correct_word)  # Set of all possible correct letters

    # Initialize some values
    guessed_letters = set()
    lives = 8
    won = False

    # Run loop until remaining lives not 0
    while lives > 0:
        print()
        # Use dash '-' if user has not guessed that letter, else that letter
        guessed_word = ''.join(letter if letter in guessed_letters else '-' for letter in correct_word)
        print(guessed_word)

        if guessed_word == correct_word:  # Check if guessed word till now is correct
            # Set win to true and exit from loop
            won = True
            break

        new_letter = input("Input a letter: ")

        if len(new_letter) != 1:  # Check if letter is not 1 character
            print("You should input a single letter")
            continue  # Skip further processing, go to beginning of loop

        if not new_letter.islower():  # Check if letter is not lowercase
            print("Please enter a lowercase English letter")
            continue  # Skip further processing, go to beginning of loop

        if new_letter in guessed_letters:  # Check if user has already input this letter
            print("You've already guessed this letter")

        # Check if the guessed letter is correct
        elif new_letter in remaining_set:
            remaining_set.discard(new_letter)  # Remove guessed letter from remaining letters
        else:
            print("That letter doesn't appear in the word")
            lives -= 1  # Reduce life by 1

        guessed_letters.add(new_letter)  # Add letter to all guesses

    # Check if user won
    if won:
        print("You guessed the word!")
        print("You survived!")
    else:
        print("You lost!")
    print()


print("H A N G M A N")

# Infinite loop until user exits
while True:
    choice = input('Type "play" to play the game, "exit" to quit: ')
    if choice == 'play':
        main()
    else:
        break
