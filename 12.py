# def square(number) :
#     return int(number) * int(number)

# result = square(input('введите число:'));
# print(result + result);

















# def sayHello(name) :
#     print(f'hello {name}');


# def calculate(x, y, expression = '+'):
#     if expression == '+':
#         return x+y;
#     elif expression == '-':
#         return x-y;


# result =  calculate(34,54, '-');
# print(f'Результат калькуляции: {result}');
# sayHello(input(f"Введите свое имя{result}:"))
# sayHello()








def strToInt(a):
    return int(a)
text = input('передай последовательность чисел:')
list = list(map( strToInt,text.split(',')));
print(list);

cor = tuple(list);
cor[0] = '9ds';
print(cor);