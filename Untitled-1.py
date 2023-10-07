from colorama import init, Fore

init(autoreset=True)

# TASK 1

from math import sqrt

def task1(a, b, c):

    x1 = 0
    x2 = 0
    
    D = b**2 - 4*a*c

    if D < 0:
        print("Main domain error")
    else:
        x1 = (-b + sqrt(D))/2*a
        x2 = (-b - sqrt(D))/2*a

    if x1 == 0 or x2 == 0:
        print("Main domain error")
    else:
        print(x1, x2)

task1(-1, 7, -10)

print(Fore.GREEN + "TASK 1 PASSED!")

# TASK 2

def task2(a, b,c):
    print(a**2 + b**2 + c**2 + 2*a*b + 2*a*c + 2*b*c)

task2(4,5,6)

print(Fore.GREEN + "TASK 2 PASSED!")

# TASK 3

def task3(a):
    if a >= 4.5:
        print("GOAT")
    elif a > 3.5 and a < 4.5:
        print("Good")
    elif a >= 2 and a <= 3.5:
        print("Poor")
    else:
        print("Bad")

task3(4)

print(Fore.GREEN + "TASK 3 PASSED!")

# TASK 4

def task4(x, y, width, height):
    return x == 0 or x == width or y == 0 or y == height

table_width = 10
table_height = 5

ant_x = 4
ant_y = 5

if task4(ant_x, ant_y, table_width, table_height):
    print("Ant is moving")
else:
    print("Ant is staying")

print(Fore.GREEN + "TASK 4 PASSED!")

# TASK 5

def task5(month):
    months = {
        "january": 1,
        "february": 2,
        "march": 3,
        "april": 4,
        "may": 5,
        "june": 6,
        "july": 7,
        "august": 8,
        "september": 9,
        "october": 10,
        "november": 11,
        "december": 12
    }
    
    if month in months:
        print(months[month])
    else:
        print("Enter a valid month")

task5("january")

print(Fore.GREEN + "TASK 5 PASSED!")

# TASK 6

def task6(text, max_length):
    if len(text) > max_length:
        shortered_text = text[:max_length]
        return shortered_text + "..."
    else:
        return text
    
a_input = "rutrum tellus pellentesque eu tincidunt tortor aliquam nulla facilisi cras fermentum odio eu feugiat pretium nibh ipsum consequat nisl vel pretium lectus quam id leo in vitae turpis massa sed"
    
print(task6(a_input, 30))

print(Fore.GREEN + "TASK 6 PASSED!")

# TASK 7

def task7(bin):
    if bin.startswith("0b"):
        return "Binary"
    elif bin.startswith("0o"):
        return "Oktanly"
    elif bin.startswith("0x"):
        return "Dekadny"
    else:
        try:
            int(bin)
            return "Hex"
        except ValueError:
            return "undefined"
        
task7("0x")

print(Fore.GREEN + "TASK 7 PASSED!")

# TASK 8

def task8(text, new_text):
    stre = text[1:-1]
    print(stre)
    print(new_text)

task8("asdqwe", "ytyt")

print(Fore.GREEN + "TASK 8 PASSED!")

def task9(text):
    vow = "AEIOUaeiou"

    for char in text:
        if char in vow:
            return True
        else: False

task9_input = "Www!"

if task9(task9_input):
    print(True)
else: print(False)

print(Fore.GREEN + "TASK 9 PASSED!")
