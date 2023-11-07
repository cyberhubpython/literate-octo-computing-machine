mn = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12

def season(mn) -> str: 
    return ["Winter", "Spring", "Summer", "Autumn"][mn//3 %4]

def month(mn) -> str: 
    return ["Dec", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov"][mn%12]

def days(mn) -> int:
    return [31, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30][mn%12]

print(month(5))
print(season(12))
print(days(3))