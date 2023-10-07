myvar = 1;
_mySecondVar = 2;

playerNames = ['Alex', 'Jhon', 'blabla'];

alex, j, b= playerNames

print(alex);

x = 'sfsd';

def printX():
    global x
    n= 1;
    print(x);
    x = 'asdsadffsdd';

printX();

print(x);
x = 0;

age = None;

age = 19
if not age:
    print('zapolnite pole vozrast');
str1 = 'al ex';


print(str1[2])
for n in "Oybekjon":
    print(n + ' ');

# print(len(6))
# print(memoryview(b"5"))
# print(('''a\ns\td'''))
text = "hello alex";
print('alexw' in text);

print('hello'[2:3].encode());

print('Sasha, Oybek, Mohinur, Sasha2'.split(', '))

print(', '.join(['Sasha', 'Oybek', 'Mohinur', 'Sasha2']));


list1 = ['asd', 'asd', 'asd'];
print(f"{list1[2]}")

print('p1: {1}, p2: {0},'.format(2, 3));

# print('asdfdg\oooassd');
# xds= 'srerre';
# print(isinstance(xds, str))


print(range(5));
names = ['Sasha', 'Oybek', 'Mohinur', 'Sasha2'] ;
for n in range(len(names)):
    print(f'{n + 1}. {names[n]}');


print([x.upper() for x in names])