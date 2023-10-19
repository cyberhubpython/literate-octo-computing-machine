from typing import Iterator 
iterObject = iter((34,565));

print(next(iterObject));
print(next(iterObject));



class MyList(Iterator):
    def __init__(self, *args) -> None:
    
        self.items = args;
      
    def __iter__(self):
        self.count = 0;
        return self;

    def __next__(self):
        if len(self.items) < self.count :
            raise StopIteration
        x = self.items[self.count];
        self.count += 2;
        return x;
[1,2,3,4,5,6]

mylist = MyList(1,2,3,4,5,6,7)

myIter =  iter(mylist)


try :
    print(next(myIter));
    print(next(myIter));
    print(next(myIter));
    print(next(myIter));
    print(next(myIter));
    print(next(myIter));
except Exception as e:
    print(e);

my2iter = iter(mylist);
for element in mylist:
    print(element);


