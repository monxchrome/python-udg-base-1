# class Student(object):
#     name = "Stefan"
#     age = 18

# print(Student().name)

class Student(object):
    def __init__(self, name, age) -> None: 
        self.name = name
        self.age = age
        print(self.name)
        pass

    def print_info(self):
        print(f"name - {self.name}")
        print(f"age - {self.age}")

student = Student("Stefan", 18)
student.print_info()

# class Math(object):
#     def __init__(self, x) -> None:
#         self.x = x
#         pass

#     def square(self):
#         return self.x * self.x

# math = Math(5)
# print(math.square())

# class Test:
#     @staticmethod
#     def print1():
#         print(f"Hello world")

# Test.print1()
# obj = Test
# obj.print1()

# class ClassMethod:
#     @classmethod

#     def hello(cls):
#         print("Hello this is a class {}".format(cls.__name__))

# ClassMethod.hello()

# class NewClass:
#     def __new__(cls):
#         print(super(NewClass))
#         return super(NewClass, cls).__new__(cls)
    
#     def __init__(self) -> None:
#         print("init")

# obj = NewClass()