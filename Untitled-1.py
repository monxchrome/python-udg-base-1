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
