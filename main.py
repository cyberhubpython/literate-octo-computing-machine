
# currentCountry = 'Uzbekistan'
# # my countries list
# countries = [ currentCountry, 'Russia'];

# print(countries)

# print(countries.sort());

import random

def generate_secret_number():
    return random.randint(1, 10)

def get_user_guess():
    return int(input("Введите число: "))

def give_feedback(secret_number, user_guess):
    if secret_number == user_guess:
        return "Вы угадали!"
    elif user_guess < secret_number:
        return "Число больше."
    else:
        return "Число меньше."

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

if __name__ == "__main__":
    main()