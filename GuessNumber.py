import random

points = 0
answers = 2
helps = 2
attempts = 10
level = 1
helpRequest = False
guessNumber = 0

while attempts > 0:
        
    try:
        guessNumber = random.randint(1,10)
        attempts -= 1
        if level %5 == 0:
            helps += 1
            answers += 1
        
        user_input = input(f"Try to guess number. Alternatevely, ask for help - h, or ask for direct answer - a: ")

        if user_input.lower() == "h" and helps > 0:
            helpRequest = True
            helps -= 1
            print("The number is even" if guessNumber %2 == 0 else "The number is odd")
            user_input = int(input("Try to guees number: "))

            if user_input == guessNumber:
                points += 2
                print("You've guessed right")
            else:
                print("You are wrong!")
        
        elif user_input.lower() == "a" and answers > 0:
            print(f"The answer is {guessNumber}")
            answers -= 1
            points += 1
        
        elif (int(user_input)) == guessNumber:
            print("You've guessd right!")
            points += 3
        else:
            print("You are wrong!")
    except:
        print('error');

print(points)