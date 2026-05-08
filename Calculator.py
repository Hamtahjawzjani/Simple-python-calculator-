def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y


while True:

    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))
    operation = input("Choose operation (+, -, *, /): ")

    if operation == "+":
        print(addition(first_number, second_number))

    elif operation == "-":
        print(subtraction(first_number, second_number))

    elif operation == "*":
        print(multiplication(first_number, second_number))

    elif operation == "/":
        if second_number != 0:
            print(division(first_number, second_number))
        else:
            print("Error: Cannot divide by zero")

    else:
        print("Invalid operation")
        
    again = input("Do you want to continue? (y/n): ")

    if again.lower() != "y":
        print("Goodbye!")
        break
