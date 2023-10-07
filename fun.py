# def myFunc(x = 2, y = 0) :
#     if (isinstance(x, int)!= True) :
#         x = int(x);
    
#     if (y != 0) :
#         return x/y;
    
    
#     return progress(x);

#     print(x*x);
# def progress(x):
#     sum = 0;
#     for n in range(20):
#         if (n == 1):
#             sum = x*x;
#         sum*= x;
#     return sum;

# print(myFunc(input('vvedite znacheniye x:')))


def kamin(x:int,)-> int|str:
    if (x== 0):
        return 'ty chto durak ??';

    return x*23;
    

print(kamin(int('0')));

def noj(x:int) -> (int,int):
    return x, x*2;
# y1,y2 = noj(3);

# print(f'наше число {y1}, удвоенное: {y2}');

def bumaga(c, a) :
    if (c == 'vizivay') :
        return a(5);
    
    
    
    return c*4;

b = bumaga;

# print(b(noj));

print(bumaga(455, lambda y : print(f'твое число : {y}')));


