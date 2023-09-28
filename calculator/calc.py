#define addition
def add(x, y):
    return x + y

#define subtraction
def subtract(x, y):
    return x - y

#define multiplycation
def multiply(x, y):
    return x * y

#define divition
def divide(x, y):
    if y == 0:
        return "Error: divide per zero"
    return x / y

#Menu
while True:
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Inser number of choosen calcuation:")

    if choice == '5':
       print("Goodbye!")
       break

    if choice not in ('1', '2', '3', '4'):
       print("Unavable choice")
       continue

    num1 = float(input("Inser first number"))
    num2 = float(input("Inser second number"))

    if choice == '1':
       print("Resultat:", add(num1, num2))
    elif choice == '2':
       print("Resultat:", subtract(num1, num2))
    elif choice == '3':
       print("Resultat:", multiply(num1, num2))
    elif choice == '4':
       print("Resultat:", divide(num1, num2))


    