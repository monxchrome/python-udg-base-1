import random
from colorama import init, Fore

init(autoreset=True)


# string


# def test(a, b):                 
#     print(f"{a} {b}")

# test(input(), input())


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

# f string (magic string)

# def fstr(a, b):
#     print(f"Hello my name is {a} I'm {b} years old")

# fstr("Stefan", 18)


# replace


# def test():
#     d = "monday, tuesday"
#     print(d.replace("monday", "wednesday"))

# test()


# endswith / startswith


# def test(a):
#     print(a.endswith(".com"))
#     print(a.startswith("a"))

# test("a@gmail.com")

# count

# def test(a):
#     print(a.count("hello"))

# test("hello world")

# is digit

# def test(a):
#     print(a.isdigit())

# test(input("enter number or str"))


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

arr = []

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

def function():
    for i in range(0, 10):
        print(i)
        if i == 6:
            break;

function()
