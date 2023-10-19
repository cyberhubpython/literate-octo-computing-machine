class Person :
    def __init__(self, name, age, gender) -> None:
        self.name = name;
        self.age = age;
        self.gender = gender;
    

    def printAge(self):
        print(f'he is {self.age} years old');


class Male(Person):
    def __init__(self, name, age) -> None:
        super().__init__(name, age, "M")


class Female(Person):
    def __init__(self, name, age) -> None:
        super().__init__(name, age, "F")

person = Male('Sasha', 24,);
person.printAge();

