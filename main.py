# Rock, Paper, Scissors game
import random

print("Welcome to Rock, Paper, Scissors game!!")

options = ["rock", "paper", "scissors"]
player_score = 0
bot_score = 0

while True:
    # Ask the user choice
    print("--------------------------------")
    user_choice = input("Please choose your weapon (Rock/Paper/Scissors) or type Q to quit game: ").lower()

    if user_choice not in options:
        if user_choice == "q":
            break
        else:
            print("Please choose a valid option...")
            continue

    bot_choice = options[random.randrange(0, len(options))]
    print(f"Bot choice is: {bot_choice}. Your choice is: {user_choice}")

    if user_choice == bot_choice:
        print("It's a tie!")
        continue
    elif user_choice == "rock" and bot_choice == "scissors":
        print("You win this round!")
        player_score += 1
        continue
    elif user_choice == "paper" and bot_choice == "rock":
        print("You win this round!")
        player_score += 1
        continue
    elif user_choice == "scissors" and bot_choice == "paper":
        print("You win this round!")
        player_score += 1
        continue
    else:
        print(f"You loose this round.")
        bot_score += 1
        continue

print("Game finished")
print(f"Final Score: Bot: {bot_score} | You: {player_score}")
