
def get_ordered_numbers(d):
    index = 0;
    for key in d:
        d[key] = index;
        index += 1;
    return d

numbers= {1: 2, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36};

ordered_numbers = get_ordered_numbers(numbers);

# print(ordered_numbers);



# todo: #19 Нужно определить функцию которая будет
# принимать список чисел, и возвращать словарь с 
# ключами каждого элемента списка и значением которого
# будут являтся замыкания которые возвращают квадрат 
# этого числа