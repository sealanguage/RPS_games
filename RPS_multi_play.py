import fileinput
import random

rock = str("rock")
paper = str("paper")
scissors = str("scissors")

wins = int(0)

while True:
    user_action = input("Enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    # print(user_action, computer_action)
    print("You chose: ", user_action, "computer chose: ", computer_action)

    if user_action == computer_action:
        print("Both players selected " + user_action + ". It's a tie.")
    elif user_action == "rock":
        if computer_action == "scissors":
            wins = wins + 1
            print("Rock smashes scissors. You win!")
            print("wins:", wins)
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            wins = wins + 1
            print("Paper covers rock! You win!")
            print("wins:", wins)
        else:
            print("Scissors cut paper. You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            wins = wins + 1
            print("Scissors cuts paper. You win!")
            print("wins:", wins)
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
print("wins: ", wins)
