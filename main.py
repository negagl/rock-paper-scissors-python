# Rock, Paper, Scissors game
import random

print("Welcome to Rock, Paper, Scissors game!!")
player_score = 0
bot_score = 0

options_dict = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper",
}

keys = list(options_dict.keys())

while True:
    # Ask the user choice
    print("--------------------------------")
    user_choice = input("Please choose your weapon (Rock/Paper/Scissors) or type Q to quit game: ").lower()

    if user_choice not in keys:
        if user_choice == "q":
            break
        else:
            print("Please choose a valid option...")
            continue

    bot_choice = keys[random.randrange(0, len(keys))]
    print(f"Bot choice is: {bot_choice}. Your choice is: {user_choice}")

    if user_choice == bot_choice:
        print("It's a tie!")
        continue
    elif bot_choice == options_dict[user_choice]:
        print("You win this round!")
        player_score += 1
        continue
    else:
        print(f"You loose this round.")
        bot_score += 1
        continue

print("Game finished")
print(f"Final Score: Bot: {bot_score} | You: {player_score}")
