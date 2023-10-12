def myFunc(a):
  
    return a('sdf');
def newFun(a):
    print(f'hello world{a}');


newF = myFunc(lambda a : newFun(a))
# newF()


def args(*a):
    print(type(a));

args(4,5,6,7);

def user(**args):
    print(args['name']);

user( surname = "Raimov");