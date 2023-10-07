import random
from colorama import init, Fore

init(autoreset=True)

####################################

# string


# def test(a, b):                 
#     print(f"{a} {b}")

# test(input(), input())

####################################

# str operators


# a = "hello world &"                 

# print(
#     a.upper(), 
#     a.lower(),
#     a.strip("&"), 
#     a.split(","),
#     a.split(),
#     a.find("w"), 
#     a.startswith("o"), 
#     a.startswith("h"),
#     a.endswith("a"), 
#     a.endswith("d"),
#     sep="\n"
#     )

####################################

# f string (magic string)

# def fstr(a, b):
#     print(f"Hello my name is {a} I'm {b} years old")

# fstr("Stefan", 18)

####################################

# replace


# def test():
#     d = "monday, tuesday"
#     print(d.replace("monday", "wednesday"))

# test()


####################################

# endswith / startswith


# def test(a):
#     print(a.endswith(".com"))
#     print(a.startswith("a"))

# test("a@gmail.com")

####################################

# count

# def test(a):
#     print(a.count("hello"))

# test("hello world")

# is digit

# def test(a):
#     print(a.isdigit())

# test(input("enter number or str"))

####################################

# logical operators + colorama


# def function(godine):
#     print(Fore.BLUE + str(godine))
#     if godine >= 18:
#         print(Fore.GREEN + "Punljetni ste")
#     else:
#         print(Fore.RED + "Ne punljetni ste")

# function(random.randint(1, 21))


# def function(a):
#     if a.lower() == "subota" or a.lower == "nedelja":
#         print("Weekend")
#     else:
#         print("pizdec")

# function("Subota")

# def function(a):
#     print(Fore.MAGENTA + str(a))
#     if a >= 91:
#         print(Fore.LIGHTCYAN_EX + "a")
#     elif a >= 81:
#         print(Fore.LIGHTCYAN_EX + 'b')
#     elif a >= 71:
#         print(Fore.LIGHTCYAN_EX + 'c')
#     else:
#         print(Fore.LIGHTCYAN_EX + 'd')

# function(random.randint(60, 100))

# def function(temperature, period):
#     if temperature >= 25 and period == "jutro":
#         print(Fore.CYAN + "Jutro 25 stepeni")
#     elif temperature >= 25:
#         print(Fore.CYAN + "Nije jutro ali je 25 stepeni")
#     else:
#         print(Fore.CYAN + "Nije 25 stepeni")

# function(22, "jutro")

# def function(a):
#     if a % 2 == 0:
#         print(f"Broj {a} je paren")
#     else:
#         print(f"Broj {a} je ne paren")

# function(int(input()), int(input()))

# def function(a):
#     print(f"ima recenica {Fore.LIGHTCYAN_EX + a}") if a in "hello world" else print(f"nema recenica {a}") # тернарка ( if "a" in "text" )

# function("hello")

####################################

# cycles


# for i in range(0, 11):
#     print(i)

num = 0

# while num < 11:
#     print(num)
#     num += 1

# while num < 11:
#     print(num);
#     num += 1
#     if num == 5:
#         break;

# while num < 11:
#     print(num);
#     num += 1
#     if num == 5:
#         continue;

# def function(a):
#     while a < 6:
#         print(a)
#         a += 1

#     for i in range(6):
#         if(i == 5):
#             print(i)
#         else:
#             print("Stefan Samokhval")

# function(0)

# arr = []

# def function(a):
#     for i in a:
#         print(i)
#         arr.extend(i)

# function("Python")
# print(arr)


# def function(a):
#     for i in a:
#         if i == "t":
#             print(i)
#             break;

# function("Python")

# def function():
#     for i in range(0, 10):
#         print(i)
#         if i == 6:
#             break;

# function()

# def function(a):
#     b = a.split(" ")
#     print(Fore.RED + str((len(b[0]) + len(b[1]))*2 ))
#     print(Fore.RED + str(len(b[0]) * len(b[1])))


# function("Artifical Intelligence")

# for i in range(1,5):
#     for j in range(6,10):
#         print(i, j)

# def function(a, b, c):
#     for i in a:
#         for j in b:
#             for k in c:
#                 print(a, b, c)

# function("Hello", "World", "Pizdec")

# for i in range(5):
#     for j in range(5, 10):
#         for k in range(10, 15):
#             print(i*j*k)

####################################

# Practice

# array (list)

# kvadrati = [x**2 for x in range(5)]
# print(kvadrati)

# arr = []
# arr2 = []

# def function(start, end):
#     for i in range(start, end+1):
#         arr.append(i)
    
#     for index in arr: 
#         if index % 2 == 0:
#             if index % 5 != 0:
#                 arr2.append(index**2)
#                 print(Fore.RED + str(sum(arr2)))


# function(int(input()), int(input()))

# def function(a):
#     print(sum(map(int,str(a))))
    

# function(int(input()))

# def function(a):
#     b = 0

#     for i in a:
#         if i == "e" or i == "E":
#             b += 1
    
#     print(b)

# function("Heeeello")

####################################

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

print(Fore.GREEN + "TASK 3 PASSED!")

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

print(Fore.GREEN + "TASK 3 PASSED!")

# TASK 6

def task6(text, max_length):
    if len(text) > max_length:
        shortered_text = text[:max_length]
        return shortered_text + "..."
    else:
        return text
    
input = "rutrum tellus pellentesque eu tincidunt tortor aliquam nulla facilisi cras fermentum odio eu feugiat pretium nibh ipsum consequat nisl vel pretium lectus quam id leo in vitae turpis massa sed"
    
print(task6(input, 30))
