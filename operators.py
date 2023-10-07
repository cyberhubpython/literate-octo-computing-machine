print(4+3)
print(4-5)
print(8*4)
print(int(4/2))

x = 6;
y= 0;

if y != 0:
    print(x/y)

else:
    print('oshibka deleniya na nol\'');

print('asd');

print(5%3);

print(4**3);

print(5//3);


x = 4;
# x = x -2;
x -= 2;

print(f"x: {x}");
x+=5
print(x);

x = x & 10
print(x);

print(20 <= 22);

print(False and False)

print(False or False);

age = 16

if age > 12 and age < 18:

    print('подросток');

car1 = 'Tesla'
car1color = 'black'
car2 = 'Merc'
car2color = 'red'

if car1color == 'red' or car2color == 'red':
    print('есть');
if car1 == 'Nexia' or car2 == 'Nexia':
    print('нексиа');

print(not(not(False or True)));
print('--------------------');
def isEquals (x, y, a):
    print(f'this is equals function {a}');
    return x == y;

# print(isEquals(4, 4, 1) and isEquals(5, 5,2) and isEquals(5,7, 3));

print((isEquals(5,3,1) or isEquals(3,4,2) )or isEquals(5,4,3));

print('-----------');

str1 = 'sd';
a = 'sd';


print(str1 is a, str1, a);
print('--------')

print(123 == '123')
print(2 not in [1,2,4])

print(6+ -3);

_m = 3;

print('Hello' is "Hello");