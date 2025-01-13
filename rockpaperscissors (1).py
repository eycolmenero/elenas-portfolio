
#1/7/25
#init
import random
wins = 0
losses = 0
ties = 0
#function
#main
def rockpaperScissors():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        global wins
        global losses
        global ties
        player = input("Rock, Paper, Scissors, Shoot:")
        computer = random.randint(1, 3)
        if computer==1:
            computer ="Rock"
        elif computer==2:
            computer="Paper"
        else:
            computer="Scissors"
        if player.capitalize() == "Rock" and computer == "Rock":
            print("The computer picked Rock, it's a tie! Play Again!")
            ties=ties+1
        elif player.capitalize() == "Rock" and computer == "Paper":
            print("The computer picked Paper, you lost! Play Again!")
            losses=losses+1
        elif player.capitalize() == "Rock" and computer == "Scissors":
            print("The computer picked Scissors, you win! Play Again!")
            wins=wins+1
        elif player.capitalize() == "Paper" and computer == "Rock":
            print("The computer picked Rock, you win! Play Again!")
            wins=wins+1
        elif player.capitalize() == "Paper" and computer == "Paper":
            print("The computer picked Paper, it's a tie! Play Again!")
            ties=ties+1
        elif player.capitalize() == "Paper" and computer == "Scissors":
            print("The computer picked Scissors, you lost! Play Again!")
            losses=losses+1
        elif player.capitalize() == "Scissors" and computer == "Rock":
            print("The computer picked Rock, you lost! Play Again!")
            losses=losses+1
        elif player.capitalize() == "Scissors" and computer == "Paper":
            print("The computer picked Paper, you win! Play Again!")
            wins=wins+1
        elif player.capitalize() == "Scissors" and computer == "Scissors":
            print("The computer picked Scissors, it's a tie! Play Again!")
            ties=ties+1
        end = input("Would you like to play again? Y or N: ")
        if end.upper() == "Y":
            print("Continuing! Currect scores are wins="+str(wins)+", losses="+str(losses)+", ties="+str(ties)+"!")
        else:
            print("Thanks for playing! Scores are wins="+str(wins)+", losses="+str(losses)+", ties="+str(ties)+"!")
            break
rockpaperScissors()
