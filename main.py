from time import time

def timer(a):
    print(a);
    def dec(fn):
        print('decorated', fn.__name__);
        def f(*arg, **kwargs):
            startTime = time();
            fn(*arg, **kwargs);
            endTime = time();
            print(endTime - startTime);
        return f;
    return dec;

@timer('osnova')
def main (a):
    for x in range(1000000):
        print(x, a);

@timer('osnova2')
def main2(a,b):
    print('asd', a, b);



# main('as');
# main2('asf', 'asg');