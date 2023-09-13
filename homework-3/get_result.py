import csv
import json

from files import BOOKS_FILE_PATH, USERS_FILE_PATH

# Чтение данных из books.csv
books = []
with open(BOOKS_FILE_PATH, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        books.append(row)

# Чтение данных из users.json
with open(USERS_FILE_PATH, 'r') as jsonfile:
    users = json.load(jsonfile)

# Распределение книг между пользователями
num_books = len(books)
num_users = len(users)
books_per_user = num_books // num_users
remainder = num_books % num_users

result = []

for user in users:
    user_data = {
        "name": user["name"],
        "gender": user["gender"],
        "address": user["address"],
        "age": user["age"],
        "books": []
    }

    # Распределение книг пользователям
    user_books = books[:books_per_user]
    books = books[books_per_user:]

    if remainder > 0:
        user_books.append(books.pop(0))
        remainder -= 1

    user_data["books"] = user_books
    result.append(user_data)

# Сохранение данных в result.json
with open('result.json', 'w') as jsonfile:
    json.dump(result, jsonfile, indent=4)
