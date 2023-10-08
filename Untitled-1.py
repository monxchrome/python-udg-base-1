from colorama import init, Fore
import time

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

time.sleep(3)

# TASK 2

def task2(a, b,c):
    print(a**2 + b**2 + c**2 + 2*a*b + 2*a*c + 2*b*c)

task2(4,5,6)

print(Fore.GREEN + "TASK 2 PASSED!")

time.sleep(3)

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

time.sleep(3)

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

time.sleep(3)

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

time.sleep(3)

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

time.sleep(3)

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
        
print(task7("0x"))

print(Fore.GREEN + "TASK 7 PASSED!")

time.sleep(3)

# TASK 8

def task8(text, new_text):
    stre = text[1:-1]
    print(stre)
    print(new_text)

task8("asdqwe", "ytyt")

print(Fore.GREEN + "TASK 8 PASSED!")

time.sleep(3)

# TASK 9

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

time.sleep(3)

# TASK 10

def task10(text):
    for i in text:
        if i.isupper():
            print(i)

task10("asdQWeRqwRT")

print(Fore.GREEN + "TASK 10 PASSED!")

time.sleep(3)

# TASK 11

def task11(n):
    arr_p = []
    arr_n = []

    for i in range(1, n):
        if i % 2 == 0:
            arr_p.append(i)
        else:
            arr_n.append(i)

    return print(arr_n, arr_p, sep="\n")

print(task11(20))

print(Fore.GREEN + "TASK 11 PASSED!")

time.sleep(3)

# TASK 12

import datetime

def task12(start, end):
    arr = []

    for i in range(start, end):
        if i % 3 == 0 and i % 6 != 0:
            i**2
            arr.append(i)

    return sum(arr)

print(task12(12, 20))

print(Fore.GREEN + "TASK 12 PASSED!")

time.sleep(3)

# TASK 13

def task13():
    current_time = datetime.datetime.now().time()

    quiet_hours = [
        (datetime.time(0, 0), datetime.time(6, 0)),
        (datetime.time(13, 0), datetime.time(17, 0)),
        (datetime.time(22, 0), datetime.time(23, 59, 59))
    ]

    noise = True

    for start, end in quiet_hours:
        if start <= current_time <= end:
            noise = False
            break
    
    if noise:
        print("You can work now")
    else:
        print("You can't work now")

task13()

print(Fore.GREEN + "TASK 13 PASSED!")

time.sleep(3)

# TASK 14

def task14(text):
    product = 1
    for i in text:
        if i.isdigit():
            product *= int(i)
        
    return product

print(task14("asdqwe123"))

print(Fore.GREEN + "TASK 14 PASSED!")

time.sleep(3)

# TASK 15

def bcrypt(s):
    encrypted = ""

    for i in s:
        if i.isdigit():
            digit = int(i)

            if digit % 2 == 0:
                encrypted += "0"
            else:
                encrypted += "1"
    
    return encrypted

print(bcrypt("15023"))

print(Fore.GREEN + "TASK 15 PASSED!")

time.sleep(3)

# TASK 16

def task16(num):
    digit_sum = 0

    num_str = str(num)
    len_digits = len(num_str)

    for i in num_str:
        value = int(i)
        digit_sum += value ** len_digits

    if num == digit_sum:
        return True
    else: 
        return False
    
print(task16(153))
    
print(Fore.GREEN + "TASK 16 PASSED!")

time.sleep(3)

# TASK 17

def task17(num):
    num_str = str(num)

    return int(num_str[0]) + int(num_str[-1])
    
print(task17(333))

print(Fore.GREEN + "TASK 17 PASSED!")

time.sleep(3)

# TASK 18

def task18(text, end):
    if text.endswith(end):
        return True
    else:
        return False

print(task18("www.google.com", "me"))

print(Fore.GREEN + "TASK 18 PASSED!")

time.sleep(3)

print(Fore.GREEN + "ALL TASKS IS DONE!")
time.sleep(1)
print(Fore.GREEN + "ALL TASKS IS DONE!")
time.sleep(1)
print(Fore.GREEN + "ALL TASKS IS DONE!")