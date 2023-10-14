# arr = [1, "asd", True, [1, 5]]

# print(len(arr)) # length of array
# print(arr[1]) # index 1 of array
# print(arr[1:3]) # from index 1 to 3

# arr2 = [5,3]
# print(arr+arr2) # array 1 + array 2 in the end
# print(arr2*2) # array 2 p. 2

# arr.append("test") # add test in the end
# print(arr)

# arr.pop() # delete test
# arr.pop(1) # delete index 1
# print(arr)

# arr.reverse() # reversing array
# print(arr)

# arr3 = [5,1,3,4,5,6]
# arr3.sort() # sorting 
# print(arr3)
# print(arr3.count(5)) # count numbers 5

# arr4 = ["hello", "world", 5]
# arr3.extend(arr4) # arr3 extends arr4
# print(arr3)

# arr4.insert(2, 5, ) # insert element 5 twice
# print(arr4)

# arr4.remove(5) # remove element 5
# print(arr4) 

# arr4.clear # clears all elements in arr4
# print(arr4)

# array = [1,2,4]
# array2 = array
# array2[1] = 9
# print(array2)
# print(array)

# array3 = [2,5,2]
# array4 = list(array3)
# array4[1] = 9
# print(array3)
# print(array4)

# zadataki

# def z1():
#     i = 0
#     arr = [1,2,3,4,5,6,7,8,9,10]
#     arr2 = []
#     arr3 = []

#     while i < len(arr):
#         if arr[i] % 2 == 0:
#             arr2.append(arr[i])
#             arr.pop(i)
#         else:
#             arr3.append(arr[i])
#             arr.pop(i)
#     return arr, arr2, arr3

# print(z1())

# def z2():
#     products = []

#     while True:
#         input_user = input()
#         if input_user == "exit":
#             break
#         products.append(input_user)
    
#     return products

# print(z2())

# set

# obj = {
#     "name": "Stefan",
#     "surname": "Samokhval",
#     "age": 18,
#     "is_studying": True
# }

# print(obj)

# name=obj["name"] # vityanut obj

# print(name)

# obj["name"] = "Hello" # update obj

# print(obj)

# obj["is_work"] = True # add obj

# print(obj)

# def za1(name, surname):
#     obj = {}

#     obj["name"] = name
#     obj["surname"] = surname

#     return obj

# print(za1(input(), input()))

# def za2(objects, balls):
#     obj = {}

#     while True:
#         if objects != "exit":
#             obj[objects] = balls
#         else:
#             break

#     return obj

# print(za2(input(), input()))
