import random

while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("Select your weapon: rock, paper or scissors: ").lower()

    if player == computer:
        print("Computer: " + computer)
        print("Player: " + player)
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("Computer: " + computer)
            print("Player: " + player)
            print("Computer Wins, paper beats rock")
        if computer == "scissors":
            print("Computer: " + computer)
            print("Player: " + player)
            print("Player Wins, rock beats scissors")
    elif player == "paper":
        if computer == "scissors":
            print("Computer: " + computer)
            print("Player: " + player)
            print("Computer Wins, scissors beats paper")
        if computer == "paper":
            print("Computer: " + computer)
            print("Player: " + player)
            print("Player Wins, paper beats rock")
    elif player == "scissors":
        if computer == "rock":
            print("Computer: " + computer)
            print("Player: " + player)
            print("Computer Wins, rock beats scissors")
        if computer == "paper":
            print("Computer: " + computer)
            print("Player: " + player)
            print("Player Wins, scissors beats paper")

    play_again = input("Play again? (yes/no)").lower()
    if play_again != "yes":
        break

print("Thank you for playing!")


