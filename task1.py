import random;

books = ['Garri Potter', 'Vlastelin kolec', 'Malinkiy princ'];

def randBook(cb = None) :
    rb = books[random.randrange(0, len(books))]
    
    if cb == None :
        return rb;
    elif cb != rb:
        return rb;
    else: 
        return randBook(cb)

currentBook = randBook();

isPurchased = False;

while isPurchased != True:
    print(currentBook);
    if input('Пойдет ?[y/n]') == 'y':
        print('спасибо за выбор! ');
        price = int(input('введите желаемую сумму покупки:'));
        if price >= 500:
            print('спасибо за покупку');
            isPurchased = True;
            continue;
        else:
            print("слишком дешево");
        
    currentBook = randBook(currentBook);