import random

RPS = {
    "R": "Rock",
    "P": "Paper",
    "S": "Scissors"
}

player = {"R": 0, "P": 1, "S": 2}

compDict = {"R": 2,"P": 0, "S": 1}

def users_move():
    users_choice = input("Please type down on of the following (R, P, or S): ")
    while users_choice not in RPS.keys():
        print("You've written something wrong. Please, rewrite you choice")
        users_choice = input("Enter your choice again: ")
    return users_choice

def computers_move():
    choices = list(RPS.values())
    return random.choice(choices)

def winner(users_choice, computers_choice):
    if users_choice==computers_choice: 
        return "That was a draw"
    elif users_choice == RPS["R"]: 
        return "You win" if computers_choice== RPS["S"] else "You lost"
    elif users_choice == RPS["P"]: 
        return "You win" if computers_choice == RPS["R"] else "You lost"
    elif users_choice == RPS["S"]: 
        return "You win" if computers_choice == RPS["P"] else "You lost"

def game_start():
    print("Let's get started!")
    
    count = 0
    ammount = int(input('How many attempts do you want? '))
    while count < ammount:
        users_choice = users_move()
        computers_choice = computers_move()
        print(f"Your choice was {users_choice}. Computer's choice was {computers_choice}.") 
        result = winner (RPS[users_choice], computers_choice)
        print(result)
        count +=1
    print()
game_start()

