num1 = 10
num2 = 0
# print(num1/num2)
# ZeroDivisionError
# we put try except
try:
    print(num1/num2)
except:
    print("Error")

# try:
       # Some Code.... 

# except:
       # optional block
       # Handling of exception (if required)

# else:
       # execute if no exception

# finally:
      # Some code .....(always executed)

dict = {'a': 1, 'c': 2}
try:
    key = input("key:")
    value = dict[key]
    print(value)
except KeyError:
    print("...")

try:
    num1 = int(input("num1: "))
    num2 = int(input("num2: "))
    result = num1 / num2
except ValueError:
    print("...")
except ZeroDivisionError:
    print("0...")
else:
    print(result)
finally:
    print()
def palindrom(text):
    rews = [text[-i] for i in range(1,len(text)+ 1)]
    if text == ''.join(rews):
        return True
    else:
        return False
    
print(palindrom("anavolimilovana"))

summa = lambda x, y: x + y
print(summa(5, 6))

take = lambda x, y: x - y
print(take(5, 6))

mix = lambda x, y, z: x + y - z
print(mix(5, 6, 7))

komb = lambda x, y, z: x * y + z
print(komb(5, 6, 6))

def stepen(n):
    return lambda x: x**n

result = stepen(5)
print(result(2))

# recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

def kvadrat(x):
    return lambda y: x**y
result = kvadrat(2)
print(result(5)) 


def limits(n, lim):
    if n < lim:
        return "ys"
    else:
        print(n)
        return limits(n-1, lim)
print(limits(3, 0))


import math
def sherlockAndMinimax(arr, p, q):
    arr1 = []
    M = [i for i in range(p, (q+1))]
    for j in range(0, len(arr)):
        arr1.append([int(math.fabs(arr[j] - i)) for i in range(p, (q+1))])
    m = []
    for i in range(0, len(arr1[0])):
        time = [arr1[j][i] for j in range(0, len(arr1))]
        m.append(min(time))
        print(time, m)
    ind= m.index(max(m))
    return M[ind]
result = sherlockAndMinimax([3, 5, 7, 9], 6)
print(result)

def suma(n):
    if n > 0:
         return 1 + suma(n-1)
suma(10)
import os

files = open("efnef.txt")
print(files.read())
print(files.readlines())
os.remove("efnef.txt")

with open("zadatak1.txt") as fajl:
    def printer(h):
        res = fajl.readlines()
        stanovi = [int(((res[i]).split(',')[2])[:-2]) for i in range(0, len(res))]
        print(stanovi)
        maxi = max(stanovi)
        print(maxi)
        for i in range(0, len(res)):
            if (res[i]).split(',')[0] == h and int(((res[i]).split(',')[2])[:-2]) == maxi:
                print ((res[i]).split(',')[1])
                break
    printer(input())
list_of_tasks = []
while True:
    user_input = input("\n1: add task \n2: lookup tasks \n3: mark completed \n4: exit \n")
    try:
        if int(user_input) == 1:
            list_of_tasks.append(input("\nenter task: "))
        elif int(user_input) == 2:
            print(list_of_tasks)
        elif int(user_input) == 3:
            try:
                list_of_tasks.remove(input("\ntype task which is completed: "))
            except:
                print("\nnot in list")
        elif int(user_input) == 4:
            print('\ncao')
            break
    except:
        print("incorrect!")
