import random;

# def hello():
#     print('Hello');
#     hello();

# hello()



def play(p1 = 10, p2= 10):
    
    a1 =int(input('a 1:'));
    a2 = int(input('a2:'));

    if random.randrange(1,5) == a1:
        p2 -= a1;

    if  random.randrange(1,5) == a2:
        p1 -= a2;
    
    print(f'h1: {p1}; h2: {p2}');
    if p1 > 0 and p2 > 0:
        return play(p1, p2);
    elif p1> p2:
        print('won p1');
    elif  p2 > p1:
        print('won p2');
    else: 
        print('dead heat');


play(5,10);