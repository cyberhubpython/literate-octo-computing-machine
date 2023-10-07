s = "sdfdsf";

class Animal:
    x = 234;
    def __init__ (this, name):
        this.name = name;
    def fda(self): 
        pass
    def setName(this, name):
        this.name = name;
    def voice(this):
        print('oshibka');
       
    def __str__(self) -> str:
        return f'object: Animal(name={self.name})'
    
class Cat(Animal):
    def __str__(self) -> str:
        return f'object: Cat(name={self.name})'
    def voice(this):
        print('meow');
    
class Dog(Animal):
    def voice(this):
        print('bark');

animal = Dog(name='Gora');





# print(animal);
# animal.fda();
# animal.voice()

# animal2 = Animal(name="Dog");
# print(animal2.name);
# animal2.x = 'Horse';
# animal2.voice();

# print(animal);
# # del animal2;
# print(animal.x);


dog = Dog(name='Gora');

dog.voice();
print(dog);
cat = Cat(name="murlik");
cat.voice();
print(cat);

