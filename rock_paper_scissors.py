import random

def main():
    print("Hello user! Let's play a game of Rock, Paper, Scissors!")
    print("\n")
    print("Here are the rules of Rock, Paper, Scissors:")
    print("Two players secretly pick one of 'rock,' 'paper,' or 'scissors.' Both players reveal their selection to the other player at once; the winner is chosen based on what the selections are. Rock beats scissors (by crushing them); scissors beats paper (by cutting it); and paper beats rock (by covering it). If both players select the same one, it is a tie.")
    print("\n")
    print("Type in your selection (rock, paper, or scissors)")
    userSelection = input()
    computerSelection = random.choice(["rock", "paper", "scissors"])
    print("The computer said {}!".format(computerSelection))
    result = None
    if userSelection == computerSelection:
        result = "tie"
    elif userSelection == "rock":
        if computerSelection == "paper":
            result = "lose"
        else:
            result = "win"
    elif userSelection == "paper":
        if computerSelection == "rock":
            result = "win"
        else:
            result = "lose"
    else:
        if computerSelection == "rock":
            result = "lose"
        else:
            result = "win"
    if result == "tie":
        print("It was a tie!")
    elif result == "win":
        print("You won!")
    else:
        print("You lost!")

if __name__ == "__main__":
    main()

