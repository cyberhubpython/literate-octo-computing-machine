import random

p1 = 12;
p2 = 12;


while p1 > 0 and p2 > 0:
    a1 = int(input('Введите силу удара(1-5) (1):'));

    a2 = int(input('Введите силу удара(1-5) (2):'));


    if a1 == random.randrange(1,5):
        p2 = p2 - a1


    if a2 == random.randrange(1,5):
        p1 -= a2

    print(f"health 1: {p1}; health 2: {p2}");

if p1 > p2 :
    print('p1 won!');
elif p1 < p2:
    print('p2 won!');
else :
    print('draw');















# import random

# player1 = 10;
# player2 = 10;

# while player1 >= 0 and player2 >= 0:
#     ataka1 = int(input("Введи свою силу удара(1-5) 1:"));


#     if ataka1 == random.randrange(1,5):
#         player2 = player2 - ataka1


#     ataka2 = int(input("Введи свою силу удара(1-5) 2:"));


#     if ataka2 == random.randrange(1,5):
#         player1 = player1 - ataka2
#     print(f"h1: {player1}, h2: {player2}")
# if player1 > player2: 
#     print("player 1 won!");
# elif player2 > player1 :
#     print("player 2 won")
# else:
#     print('dead heat')