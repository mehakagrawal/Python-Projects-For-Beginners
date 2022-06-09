import random

while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)

    player = None

    while player not in choices:
        player = input("Choose from rock, paper, or scissors: ").lower()

    if player == computer:
        print("Computer:",computer)
        print("It's a Tie!")
    elif player == "rock":
        if computer == "paper":
            print("Computer:",computer)
            print("You lose!")
        elif computer == "scissors":
            print("Computer:",computer)
            print("You won!")
    elif player == "paper":
        if computer == "rock":
            print("Computer:",computer)
            print("You won!")
        elif computer == "scissors":
            print("Computer:",computer)
            print("You lose!")
    elif player == "scissors":
        if computer == "rock":
            print("Computer:",computer)
            print("You lose!")
        elif computer == "paper":
            print("Computer:",computer)
            print("You win!")
    
    play_again = input("Do you want to play again (yes/no)?: ").lower()

    if play_again != "yes":
        break

print("Thanks for playing the game!")