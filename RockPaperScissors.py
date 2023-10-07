import random

# def attempts_amount():
#     ask_attempts_amount = int(input("Enter amount of attemtps you are willing to have. The number must be odd: "))
#     if ask_attempts_amount %2 == 0: print("Its an even number")
#     else: print("Thank you for you choice. Let's get started!")

def users_move():
    users_choice = input("Please type down on of the following (Rock, Paper, or Scissors): ")
    while users_choice not in ("Rock", "Paper", "Scissors"):
        print("You've written something wrong. Please, rewrite you choice")
        users_choice = input("Enter your choice again: ")
    return users_choice

def computers_move():
    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)

def winner(users_choice, computers_choice):
    if users_choice==computers_choice: return "That was a draw"
    elif users_choice == "Rock": return "You win" if computers_choice== "Scissors" else "You lost"
    elif users_choice == "Paper": return "You win" if computers_choice == "Rock" else "You lost"
    elif users_choice == "Scissors": return "You win" if computers_choice == "Paper" else "You lost"

def game_start():
    print("Let's get started!")
    while True:
        users_choice = users_move()
        computers_choice = computers_move()
        print(f"Your choice was {users_choice}. Computer's choice was {computers_choice}.") 
        result = winner(users_choice, computers_choice)
        print(result)

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again != "yes":
            break

game_start()