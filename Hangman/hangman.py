def main(): # Main function
    from os import system, name # Imports OS to allow us to clear the console to print the ASCII text.
    from random import choice # Import the choice function from the random library to choose a random word from our words list.
    system("cls" if name == "nt" else "clear") # Clears the terminal, should work across all operating systems.
    # List of words the program will choose from.
    words = ["apple", "banana", "mango", "strawberry",
    "orange", "grape", "pineapple", "apricot", "lemon", "coconut", "watermelon",
    "cherry", "papaya", "berry", "peach", "lychee", "muskmelon"]
    hangman = ["""\n  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========""", """\n  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========""", """\n  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========""", """\n  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========""", """\n  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========""", """\n  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========""", """\n  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n========="""] # List of ASCII hangman images
    if len(words) > 0: # Checks to see if the list of words is empty, check end of if so it will print an error, otherwise it will continue.
        word = choice(words) # Chooses a random word from our list of words.
        guesses = "" # Initiates a blank string for our list of guesses which will be used within the code and also allow the user to know what they have already guessed.
        replaced = "" # Initiates a blank string to print our already found characters and the underlines.
        for char in word: # For loop to properly create the replaced string.
            if char == " ": # Checks to see if the character is a space, if so adds a space to the replaced string.
                replaced += " "
            else: # Checks to see if the character is not a space, if so it adds an underline to the string.
                replaced += "_"
        turns = 6 # Amount of turns a user is allowed. Default amount of turns is six as that"s how many limbs will be printed, if changed limbs will not be printed.
        failed = 0 # How many times the user has failed.
        while failed != turns: # Create a while loop to keep going until the user runs out of turns.
            system("cls" if name == "nt" else "clear") # Clears the terminal.
            if turns == 6: # Checks to see if the turns is the default amount, if so it'll print out ASCII hangman image.
                print(hangman[failed])
            print(f"Word: {replaced.upper()}") # Prints our replaced string so the user knows what characters they got successfully and what else they need to get.
            right = 0 # Initiates a variable called right which will be used in the for loop below.
            for char in word: # For loop, will go through each character in the word.
                if char in guesses: # Checks to see if the character is in the guesses list and if so it'll add one to the right count.
                    right += 1
                if right >= len(word): # If the length of the word is less then or equal to the right variable the program will end and alert the user they finished successfully.
                    print("Nice job! You guessed the word correctly!")
                    return
            print(f"Guesses: {guesses.upper()}") # Prints what the user has already guessed.
            guess = input("Please provide a guess!: ") # Asks the user for a guess.
            if guess not in guesses: # If the guess they provided is not in the guesses string it will go through a for loop for each character in the guess, if the character is not in guesses it will add it.
                f = 0 # Initiates an f variable for failed.
                for char in guess:
                    if char not in guesses:
                        guesses += char
                        if char not in word:
                            f = 1 # If it does fail it won't count per character but per guess so it will set f to 1
                failed += f # Add f to failed, if they already guessed their guess it won't add anything but if they guess something that they haven't guessed before it'll add one to the failed count.

            if guess in word: # Checks to see if their guess is in the word.
                replaced = "" # Initiates the replaced string again.
                for char in word: # Looks through each character in the word.
                    if char in guesses: # If the character is in guesses it will add the character to the string.
                        replaced += char
                    elif char == " ": # If the character is a space it will add a space.
                        replaced += " "
                    else: # If the character is not in the guesses list and not a space it will add an underline.
                        replaced += "_"
        system("cls" if name == "nt" else "clear") # Clears the console.
        if turns == 6: # If the turns amount is default it will print the final ASCII hangman image.
            print(hangman[6])
        print("You had to many failed attempts, feel free to run this file again to play again!") # Alerts the user that they used up all of their attempts.
    else:
        print('Empty list of words provided, please edit the file and add at least one word to the list named "words".') # Alerts the user that the words list is empty.
main() # Calls the main function.