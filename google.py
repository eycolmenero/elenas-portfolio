#11/12/24
import random
def game():
    print("Welcome to the Number Guessing Game!")
    print("Here you will guess the random number the computer generates 3 times and see if you can beat the computer!")
    guess = int(input("Enter Guess 1: "))
    secret = random.randint(0,10)
    two = int(input("Enter Guess 2: "))
    three = int(input("Enter Guess 3: "))
    if guess == secret:
        print("Guess 1 is correct! You Win!")
    if two == secret:
        print("Guess 2 is correct! You Win!")
    if three == secret:
        print("Guess 3 is correct! You Win!")
    elif three!= secret and two != secret and guess!= secret:
        print("No right guesses, the correct answer was "+ str(secret)+", thanks for playing!")
#main
game()
