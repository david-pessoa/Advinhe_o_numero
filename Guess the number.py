from images import guess_num
from os import system
import random
def attempts(tries, think):
    win = False
    while (tries != 0) and (win != True):
        print(f"You have {tries} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        if tries != 1:
            if guess > think:
                print("Too high")
                print("Guess again")
                tries -= 1
            elif guess < think:
                print("Too low")
                print("Guess again")
                tries -= 1
            else:
                print(f"You did it! the answer was: {think}")
                win = True
        else:
            if guess > think or guess < think:
                print("You ran out of attempts. You loose.")
                print(f"The answer was: {think}")
                tries -= 1
            else:
                print(f"You did it! the answer was: {think}")
                win = True

print("Welcome to the number guessing game!")
answer = input("Would you like to play the game? Type 'yes' or 'no': ")
while answer == "yes":
    think = random.randint(1, 100)
    print(guess_num)
    mode = input("Do you want to play the hard or the easy mode? Type 'hard' or 'easy': ")
    print("I'm thinking of a number between 1 and 100")
    if mode == "easy":
        attempts(10, think)
    elif mode == "hard":
        attempts(5, think)

    answer = input("Would you like to play again? Type 'yes' or 'no': ")
    if answer == "yes":
        system("cls")
