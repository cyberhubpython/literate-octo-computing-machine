from random import randint

# x = randint(1,10)
# user_num = 0
# attempt = 0
def get_user_guess():
    return int(input("Enter your : "))
def give_feedback(secret_number, user_guess):
    if secret_number == user_guess:
        return "Great, you found it!"
    elif user_guess < secret_number:
        return "it is more than this."
    else:
        return "it is less than this."
def main():
    secret_number = generate_secret_number()
    score = 0
    help_count = 2
    exact_answer_count = 2
    level = 1
    while True:
        print("Уровень", level)
        user_guess = get_user_guess()
        feedback = give_feedback(secret_number, user_guess)
        if feedback == "Вы угадали!":
            print(feedback)
            score += 3
            break
        elif user_guess == 5:
            print(feedback)
            score += 1
            help_count -= 1
        elif help_count > 0:
            print(feedback)
            help_count -= 1
            score += 2
        else:
            print(feedback)
            break
        level += 1
        if level % 5 == 0:
            help_count += exact_answer_count
            exact_answer_count = 2
    print("Ваш результат:", score)

# while True :
#  print("Guess my number from 1 to 10")
#  user_num = int(input("Your guess:"))
#  attempt+=1
#  if user_num == x:
#   print("Great, you found it.")
#   break
#  elif user_num > x:
#   print("it is less than this")
#  elif user_num < x :
#   print ("it is more than this")