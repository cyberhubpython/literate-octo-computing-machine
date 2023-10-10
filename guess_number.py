import random;

# 1) нужно определить след переменные:
# guessNumber, points=0, helpsCount = 2, answersCount = 2, attempts = 10, isHelpRequested = false;

guessNumber = 0;
points = 0;
helpsCount = 2;
answersCount = 2;
attemptsCount = 10;
level = 1;
isHelpRequested = False

# 2) определяем цикл: 
# 2.1) зарандомить,
# 2.2) отнять одну попытку,  проверять колво уровней и на каждом 5 давать по помощи + ответу, запросить помощь/ответ/число, 
# 2.3) разбить ответ, 
# 2.3.1) если у нас запрашивается помощь
# 2.3.2) сокращаем количество очков
# 2.3.3) принтуем ответ помощи
# 2.3.4) убрать одну помощь, запросить след число
# 2.3.5) сравнить след число с загаданным числом
# 2.3.5.1) если число верное то дать баллы
# 2.3.5.2) если число неверно, пропустить текущий цикл
# 2.3.6)  если был запрошен точный ответ, показать загаданное число, дать баллы,  убрать один точный ответ
# 2.3.7) если ввод пользоователя не помощь и не ответ то переконвертировать ввод пользователя в инт
# 2.3.8) сравниваем загаданное число с ответом пользователя
# 2.3.9) если все хорошо, даем 3 балла
# 2.3.10) иначе говорим то что он ошибся
# 3) завершение игры
# 3.1) спросить имя игрока,
# 3.2) поздравить игрока с набранными очками, и показать его уровень

while attemptsCount > 0 :
    guessNumber = random.randint(1,10);
    attemptsCount -= 1;
    if level % 5 == 0 :
        helpsCount +=1
        answersCount +=1
    

    userInput = input(f'угадай загаданное число, или запроси попытку(h={helpsCount}) или ответ(a={answersCount}): ');

    if userInput == 'h':
        isHelpRequested = True
        helpsCount-=1;
        print('число больше 5' if guessNumber > 5 else 'число меньше 5')
        userInput = int(input('напиши число: '));
        
        if userInput == guessNumber:
            points +=2;
            print('угадал');
        else:
            print('не угадал');
    elif userInput == 'a' :
        print(f'загаданное число: {guessNumber}');
        points+=1
        answersCount -=1
    elif int(userInput) == guessNumber :
        points +=3;
        print('ты угадал')
    else:
        print('ты не угадал');

print(points);