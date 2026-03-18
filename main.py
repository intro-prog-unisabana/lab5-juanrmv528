from utils import *

while True:
    op = input("Which calculation would you like to perform? (add, subtract, multiply, divide, exponent, modulo, floor_divide, absolute, exit):\n").lower()

    if op == "exit":
        break

    if op not in ["add", "subtract", "multiply", "divide", "exponent", "modulo", "floor_divide", "absolute"]:
        print("Invalid option!")
        continue

    if op == "absolute":
        num = float(input("Enter the number:\n"))
        print(f"The result is: {absolute(num)}")
    else:
        a = float(input("Enter the first number:\n"))
        b = float(input("Enter the second number:\n"))

        if op == "add":
            res =   (a, b)
        elif op == "subtract":
            res = sub(a, b)
        elif op == "multiply":
            res = multiply(a, b)
        elif op == "divide":
            res = divide(a, b)
        elif op == "exponent":
            res = exponent(a, b)
        elif op == "modulo":
            res = modulo(a, b)
        elif op == "floor_divide":
            res = floor_divide(a, b)

        print(f"The result is: {res}")