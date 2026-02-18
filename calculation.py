def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b

def floor_divide(a, b):
    if b == 0:
        return "Error: Cannot perform floor division by zero."
    return a // b

def power(a, b):
    return a ** b

def modulus(a, b):
    if b == 0:
        return "Error: Cannot perform modulus by zero."
    return a % b


def display_menu():
    print("\n========== PYTHON CALCULATOR ==========")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Floor Division (//)")
    print("6. Power (**)")
    print("7. Modulus (%)")
    print("8. Exit")
    print("=======================================")


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def main():
    while True:
        display_menu()
        choice = input("Select an operation (1-8): ")

        if choice == '8':
            print("Exiting calculator. Goodbye!")
            break

        elif choice in ['1', '2', '3', '4', '5', '6', '7']:
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")

            if choice == '1':
                result = add(num1, num2)
            elif choice == '2':
                result = subtract(num1, num2)
            elif choice == '3':
                result = multiply(num1, num2)
            elif choice == '4':
                result = divide(num1, num2)
            elif choice == '5':
                result = floor_divide(num1, num2)
            elif choice == '6':
                result = power(num1, num2)
            elif choice == '7':
                result = modulus(num1, num2)

            print("Result:", result)

        else:
            print("Invalid choice! Please select from 1 to 8.")


if __name__ == "__main__":
    main()
