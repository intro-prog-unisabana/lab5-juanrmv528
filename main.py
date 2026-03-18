from utils import add, sub, multiply, divide, exponent, modulo, floor_divide, absolute

while True:
    opcion = input(
        "Which calculation would you like to perform? "
        "(add, subtract, multiply, divide, exponent, modulo, floor_divide, absolute, exit):\n"
    ).lower()

    # salir
    if opcion == "exit":
        break

    # validar opción
    if opcion not in [
        "add", "subtract", "multiply", "divide",
        "exponent", "modulo", "floor_divide", "absolute"
    ]:
        print("Invalid option!")
        continue

    # caso especial: absolute
    if opcion == "absolute":
        num = float(input("Enter the number:\n"))
        resultado = absolute(num)
        print(f"The result is: {resultado}")
        continue

    # pedir dos números
    num1 = float(input("Enter the first number:\n"))
    num2 = float(input("Enter the second number:\n"))

    if opcion == "add":
        resultado = add(num1, num2)

    elif opcion == "subtract":
        resultado = sub(num1, num2)

    elif opcion == "multiply":
        resultado = multiply(num1, num2)

    elif opcion == "divide":
        resultado = divide(num1, num2)

    elif opcion == "exponent":
        resultado = exponent(num1, num2)

    elif opcion == "modulo":
        resultado = modulo(num1, num2)

    elif opcion == "floor_divide":
        resultado = floor_divide(num1, num2)

    print(f"The result is: {resultado}")