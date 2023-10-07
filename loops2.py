for item in ['banana', 'apple']:
    continue;
    print(item);
    break;
else:
    print('мы все пересчитали');

l = ['banana', 'apple', 'banana', 'apple' ,'banana', 'apple', 'pineapple'];

l2 = [];
index = 0;
while   len(l) > index :
    index +=1;
    if l[index -1] in l2 : 
        continue;
    l2.append(l[index-1]);
    print(l[index-1]);
    if index == 2:
        break
else:
    print('мы удалили дубли');

print(l2);

def w() :
    print('hello world');
    if input('povtorit?') == 'y': 
        w();


    


# w();

def fun2() :
    return True;
while fun2():
    print('зеуепав');