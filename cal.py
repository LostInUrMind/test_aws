
num1 = input("Enter num1 :")
num2 = input("Enter num2 :")
op = input("Operation: ")

try:
    num1 = float(num1)
    num2 = float(num2)
    result = None

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero")
    else:
        print("Error: Invalid operation")

    if result is not None:
        print(f"{num1} {op} {num2} = {result}")
except Exception:
    print("Error: Invalid input. Please enter a number.")