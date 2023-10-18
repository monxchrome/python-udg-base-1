from __future__ import print_function, unicode_literals
from InquirerPy import prompt

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

def task7():
    arr = []

    with open("hex.txt", "r") as file:
        lines = file.readlines()

    for i in lines:
        if i.startswith("0x"):
            hex_number = int(i, 16)
            if str(hex_number).endswith("3"):
                arr.append(hex_number)
        else:
            continue

    return sum(arr)

print(task7())

def task8():
    event = []

    while True:
        user_input = input()

        if user_input == "exit":
            break

        event.append(user_input)
    
    return event

print(task8())

def task9():
    films = ["Trancedence", "Fast and Furious 8", "Need for Speed", "Anabel"]
    favourite_films = []
    watched_films = []

    questions = [
        {
            'type': 'list',
            'name': 'action',
            'message': 'Menu',
            'choices': ['All films', 'Add film', 'Add favourite film', 'Watched films', 'Exit']
        }
    ]

    while True:
        answers = prompt(questions)
        action = answers['action']

        if action == 'All films':
            print("All films: ")

            for film in films:
                print(film)

        elif action == 'Add film':
            new_film = input("Input name of the film: ")

            films.append(new_film)
            
            print(f"Movie '{new_film} was added'")

        elif action == 'Add favourite film':
            favorite_choices = [
                {
                    'type': 'list',
                    'qmark': '❤',
                    'message': 'Choise a favourite film: ',
                    'name': 'favorite_films',
                    'choices': films
                }
            ]

            favorite_answers = prompt(favorite_choices)
            selected_favorite_films = favorite_answers['favorite_films']
            print(selected_favorite_films)

            if selected_favorite_films:
                print("Favourite film: ")
                favourite_films.append(selected_favorite_films)
                print(selected_favorite_films)
            else:
                print("You haven't chosen any movie")

        elif action == 'Watched films':
            watched_films = [
                {
                    'type': 'list',
                    'qmark': '✔',
                    'message': 'Select movies that have been watched: ',
                    'name': 'watched_films',
                    'choices': films
                }
            ]
            watched_answers = prompt(watched_films)
            selected_watched_films = watched_answers['watched_films']

            if selected_watched_films:
                watched_films.append(selected_watched_films)
                films.remove(selected_watched_films)
                    
                print("Film has been added to last watched ")
            else:
                print("You haven't chosen any movie")

        elif action == 'Exit':
            break

task9()
