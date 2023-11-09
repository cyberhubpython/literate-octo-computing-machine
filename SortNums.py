Num = [35, 80, 90, 73, 46, -65, "abc", "46"]

# def Square(Num):
#     return sorted([x ** 2 for x in Num])

def Square2(Num):
    squareVar = []
    for x in Num:
        try:
            squareVar.append(int(x) **2)
        except:
            print ("Nice try")
    return sorted(squareVar)
        
# print (Square(Num))
print (Square2(Num))