"""
This is a guessing game, a user inout a number and
the program uses that number as the max number (so you
shouldn't guess above the number u put in the first place)
so the user will keep guessing until user is correct before
the program ends
"""

import random
max_range = input("Type a number: ")

if max_range.isdigit():
    max_range = int(max_range)

    if max_range <= 0:
        print("Please type a number greater than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()

random_number = random.randint(0, max_range)
guesses = 0

while True:
    
    guesses += 1 #Tells you how many guesses the user did
    
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time. ")
        continue

    if user_guess == random_number:
        print("Correct!,you got it! ")
        break
    elif user_guess > random_number:
            print("You are above the number!, try again")
    else:
            print("You were below the number! try again")

print("You got it in", guesses, "guesses")
