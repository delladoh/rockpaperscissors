import random

choices = ["rock", "paper", "scissors"]

computer = random.choice(choices)

player = input("Select your weapon: Rock, Paper or Scissors")

print("Computer: " + computer)
print("Player: " + player)


