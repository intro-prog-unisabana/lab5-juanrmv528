    # FREEZE CODE BEGIN
    def greet(name):
        """
        Return a greeting message for the given name.

        Args:
            name (str): The name of the person to greet.

        Returns:
            str: A greeting in the format "Hello, <name>!".
        """
        return f"Hello, {name}!"


    def flip(input_string):
        """
        Reverse the characters in the given string.

        Args:
            input_string (str): The string to be reversed.

        Returns:
            str: The reversed string.
        """
        return input_string[::-1]


    def count_letters(input_string, letter):
        """
        Count how many times a specific letter appears in a string.

        Args:
            input_string (str): The string to search.
            letter (str): The letter to count (should be a single character).

        Returns:
            int: The number of occurrences of the letter in the string.
        """
        count = 0
        for char in input_string:
            if char == letter:
                count += 1
        return count

    if __name__ == "__main__":
    print("This file is being run directly.")
    # FREEZE CODE END


def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def exponent(a, b):
    return a ** b

def modulo(a, b):
    if b == 0:
        return "Error: Modulo by zero is not allowed."
    return a % b

def floor_divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a // b

def absolute(a):
    return abs(a)

