import random

def main():
    options = ["rock", "paper", "scissors"]

    # Random choice for computer
    computer = random.choice(options)

    # Take input from player
    player = input("Enter rock, paper, or scissors: ").lower()

    # Validate input
    if player not in options:
        print("Error: Invalid input! Please choose rock, paper, or scissors.")
        return

    print(f"Computer chose: {computer}")

    # Compare and print result
    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You win!")
    else:
        print("You lose!")

main()
