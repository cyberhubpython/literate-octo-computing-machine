import random;
x = 0;
while x < 5: 
    x +=1;
    if x  == 2:
        continue;
    print('asd', x);






y  = True;

while y:
    print('it is true');
    randi = random.randint(0, 10)
    y =  False if randi > 5 else True;


for element in ['apple', 'banana', 'pineapple']:
    print(element);
    if element == 'banana':
        break;
else: 
    print('мы все показали');

a = 0
while a < 2:
    print('it is true');
    a+=1;
    if a == 1: 
        break;
else:
    print('it is false');


list1 = [345,47, 567, 86768,];

sum= 0;

for num in list1:
    sum += num;
