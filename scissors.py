import random
import json


# Правила игры
rules = {
    "rock": {
        "beats": "scissors",
        "loses": "paper" },
    "scissors": {
        "beats": "paper",
        "loses": "rock" },
    "paper": {
        "beats": "rock",
        "loses": "scissors" }
}
 

computer_choice = random.choice(["rock", "scissors", "paper"])

player_choice = input("Choose: rock, scissors, paper: ")

if player_choice == computer_choice:
    print("Draw!")
elif player_choice in rules[computer_choice]["beats"]:
    print("You won!")
else:
    print("This is my fortune!") 

# count = 0 
# result = 3
# while count < result :
#         player_choice = player_choice()
#         computer_choice = computer_choice()
#         print(f"Your choice was {player_choice}. Computer's choice was {computer_choice}.") 
#         result = winner(player_choice, computer_choice)
#         print(result)
#         count +=1
# print()

  

# result=0
# while result < 3:
#  result +=1

# print (result)

# def replay(replay):
#     while 
# def count_results(results) :
#     return results [0 : 3] 

# if player_choice[0] > computer_choice[3]:
#     print ("You won")
# elif computer_choice[0] > player_choice[3]:
#     print ("I won")
# else:
#     print ("Ничья")