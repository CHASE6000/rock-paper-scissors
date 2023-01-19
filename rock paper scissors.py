import random

options = ["rock", "paper", "scissors"]

while True:
    user_choice = input("Choose rock, paper, or scissors: ")
    computer_choice = random.choice(options)
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win!")
    elif user_choice == "rock" and computer_choice == "paper":
        print("You lose!")
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win!")
    elif user_choice == "paper" and computer_choice == "scissors":
        print("You lose!")
    elif user_choice == "scissors" and computer_choice == "rock":
        print("You lose!")
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win!")
    else:
        print("Invalid choice. Please choose rock, paper, or scissors.")
