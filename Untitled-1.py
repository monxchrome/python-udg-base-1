def task1(a,b):
    elements = [item for item in a if item in b]
    return elements

print(task1(
    [1,2,3,4,5],
    [3,4,5,6,7]
))


def task2(a, max):
    count = 0

    for i in a:
        if i < max:
            count += 1
    
    return count

print(task2([1,2,3], 3))

def task3(arr, num):
    array = []

    for i in arr:
        if i % 2 == 0:
            array.append(i+3)
        else:
            array.append(i)
    
    return array

print(task3([1,2,-1,3,-4], 3))


def task4(nums):
    unique_sorted_array = sorted(set(nums), reverse = True)

    if len(unique_sorted_array) >= 2:
        return unique_sorted_array[1]
    else:
        return None
    
print(task4([11,22,33]))

def task5(password, length, flagUpper=False, flagLower=False, flagDigit=False):
    if len(password) < length:
        return False
    
    if flagUpper and not any(char.isupper() for char in password):
        return False
    
    if flagLower and not any(char.islower() for char in password):
        return False
    
    if flagDigit and not any(char.isdigit() for char in password):
        return False
    
    return True

print(task5("Passw123", 10, True, True, False))

def task6():
    max = 0

    with open("numbers.txt", "r") as file:
        lines = file.readlines()

    for i in lines:
        a, b = map(int, i.strip().split(","))

        if a == b and a * b > max:
            max = a * b

    return max

print(task6())