import random

def generate_password(length, include_uppercase=True, include_numbers=True, include_special=True):
    character = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"

    password = "".join(random.choice(character) for _ in range(length))
    return password

lenght = int(input("How many character: "))
password_gen = generate_password(lenght)

print("Password:", password_gen)
