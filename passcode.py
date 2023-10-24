#Написать программу, которая будет генерировать случайные пароли.
# Пароль должен быть длиной не менее 8 символов и содержать цифры, 
#буквы верхнего и нижнего регистра, а также специальные символы.
 
# import random 
# def generatePassword(lenght=8):
#     password= ""
#     symbols = "strings"
#     for k in range(lenght):
#         password+=random.choice(symbols)
#         return(password)
    
# password= generatePassword()
# print(password)



import random
import string


def generatePassword(length=8):
#   symbols = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-_=+[{]}\|;:,<.>/?"
    symbols = string.printable
    password = ""
    for k in range(length):
        password += random.choice(symbols)
    return password

password = generatePassword()
print(password)

    