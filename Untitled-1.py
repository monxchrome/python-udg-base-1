from __future__ import print_function, unicode_literals
from InquirerPy import prompt, inquirer

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

def task10():
    books = [
            {"name": "transcedence", "price": 10},
            {"name": "anabel", "price": 15},
            {"name": "harry potter", "price": 25},
            {"name": "NFS", "price": 20},
        ]
    
    sections = [
        {"name": "All books", "value": "all_books"},
        {"name": "Add book", "value": "add_book"},
        {"name": "Update book", "value": "update_book"}
    ]

    selected_choiсe = inquirer.select(
        message="Choose books:",
        choices = sections
    ).execute()

    if selected_choiсe == "all_books":
        print("All books:")
        for book in books:
            print(f"{book['name']} - {book['price']}")
    elif selected_choiсe == "add_book":
        add_book = inquirer.text(
            message="Add the name of book"
        ).execute()

        add_price = inquirer.text(
            message="Add price of the book"
        ).execute()

        add_price = float(add_price)

        new_book = {"name": add_book, "price": add_price}
        books.append(new_book)

        print(f"The new book {add_book} - {add_price} has been added")
    elif selected_choiсe == "update_book":
        book_name = [book['name'] for book in books]

        selected_book = inquirer.select(
            message="Choose a book to change the price:",
            choices=book_name
        ).execute()

        for book in books:
            if book['name'] == selected_book:
                new_price = inquirer.text(
                    message = "Enter the value to change price of the book"
                ).execute()

                new_price = float(new_price)

                book["price"] = new_price

                print(f"The price of {book['name']} has been changed to {new_price}")
                break
        else:
            print("Error")
    else:
        print("Error")

task10()

def task11():
    print("Hello, user, welcome to the phone number dictionary!")
name_contact = {}

def add_contact():
    name = input("Type the name: ")
    number = input("number: ")
    name_contact[name] = number
    print(f"Contact {name} added!")

def search_contact():
    name = input("Type whom you want to find: ")
    if name in name_contact:
        print(f"The phone number for {name} is - {name_contact[name]}")
    else:
        print(f"{name} is not in the book")

def change_number():
    name = input("Type who's number to change: ")
    if name in name_contact:
        new_number = input("Type new number: ")
        name_contact[name] = new_number
    else:
        print("There is no person with that name in book!")


def delete_contact():
    name = input("Type whom to delete: ")
    if name in name_contact:
        del name_contact[name]
    else:
        print("not in the book")


while True:
    print("Here are the options: \n 1) Add new contact. \n 2)search for a number by name. \n 3)Change the number of a contact. \n 4)Delete the contact. \n 5) exit ")
    choice = input()
    
    if choice == "1":
        print(name_contact)
        add_contact()
    elif choice == "2":
        print(name_contact)
        search_contact()
    elif choice == "3":
        print(name_contact)
        change_number()
    elif choice == "4":
        print(name_contact)
        delete_contact()
    elif choice == "5":
        print("Exiting phonebook. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

task11()

def task12(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return task12(n - 1) + task12(n - 2)
print(task12(int(input())))

def task13(n):
    if n < 10:
        return 1
    
    return 1 + task13(n//10)

print(task13(int(input())))

def task14(s):
    s = s.lower()
    s = ''.join(filter(str.isalnum, s))

    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return task14(s[1:-1])
    
print(task14("A man, a plan, a canal, Panama"))