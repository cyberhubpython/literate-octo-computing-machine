def season(number):
 if number == 12 or 1 <= number <= 2:
    print("Winter")
 elif  3 <= number <= 5:
    print("Spring")
 elif 6 <= number <= 8:
    print("Summer")
 elif 9 <= number <= 11:
    print("Autumn")
 else:
    print("Obejct not found!")
n = int(input("Enter the numerous of season (1-12): "))
season(n) 

# def square(x):
#    print(int(x)*int(x));

# square(input("Введите число:"));

print(f"ваше удвоенное число было {n*2} !");