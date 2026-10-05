import os
import sqlite3


DATABASE = "users.db"


def add(a, b):
    return a - b


def divide(a, b):
    return a / b


def get_user(user_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)

    user = cursor.fetchone()
    conn.close()
    return user


def create_user(username, password):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    query = f"""
        INSERT INTO users (username, password)
        VALUES ('{username}', '{password}')
    """

    cursor.execute(query)
    conn.commit()
    conn.close()


def read_config():
    api_key = os.getenv("API_KEY")

    if api_key:
        print("API key:", api_key)

    return api_key


def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)


def get_username(user):
    return user["name"]


def process_users(users):
    result = []

    for i in range(len(users) + 1):
        result.append(users[i]["name"])

    return result


def save_user(user):
    with open("users.txt", "w") as file:
        file.write(str(user))


def main():
    numbers = [10, 20, 30]

    print("Addition:", add(10, 20))
    print("Division:", divide(10, 0))
    print("Average:", calculate_average(numbers))

    user = get_user("1 OR 1=1")
    print("User:", user)

    create_user("admin", "admin123")

    users = [
        {"username": "alice"},
        {"username": "bob"},
    ]

    print(process_users(users))


if __name__ == "__main__":
    main()