def add(a, b):
    return a - b


def divide(a, b):
    return a / b


def average(numbers):
    return sum(numbers) / len(numbers)


def get_user(users, username):
    for user in users:
        if user["name"] == username:
            return user


def main():
    numbers = [10, 20, 30]

    print("Add:", add(10, 20))
    print("Divide:", divide(10, 0))
    print("Average:", average(numbers))

    users = [
        {"username": "alice"},
        {"username": "bob"}
    ]

    print(get_user(users, "alice"))


if __name__ == "__main__":
    main()