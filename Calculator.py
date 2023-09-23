def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Inappropriate opperation"
    return x / y

user_input = input("Please, type down one of the following opperations: add, subtract, multiply, or divide: ")
user_input in ("add", "substract", "multiply", "devide")
number1 = int(input('First number: '))
number2 = int(input('Second number: '))
if user_input == "add":
    print("Result: ", add(number1, number2))
elif user_input == "subtract":
    print("Result: ", subtract(number1, number2))
elif user_input == "multiply":
    print("Result: ", multiply(number1, number2))
elif user_input == "divide":
    print("Result: ", divide(number1, number2))
else:
    print("Incorrect input")