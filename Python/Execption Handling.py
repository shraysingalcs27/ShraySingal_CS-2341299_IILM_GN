print("1. Creating ArithmeticError")
try:
    x = 10 / 0
except ArithmeticError as e:
    print("ArithmeticError occurred:", e)

print("\n2. Creating ValueError")
try:
    y = int("abc")
except ValueError as e:
    print("ValueError occurred:", e)

print("\n3. Handling ArithmeticError")
try:
    a = 20
    b = 0
    print(a / b)
except ArithmeticError:
    print("Cannot divide by zero")

print("\n4. Handling ValueError")
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input! Please enter a number")

print("\n5. Handling multiple exceptions in one try")
try:
    p = int(input("Enter first number: "))
    q = int(input("Enter second number: "))
    print(p / q)
except ValueError:
    print("ValueError: Invalid number")
except ZeroDivisionError:
    print("ZeroDivisionError: Cannot divide by zero")

print("\n6. Calculator with 4 operations and maximum exception handling")
try:
    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))
    op = input("Enter operation (+, -, *, /): ")

    if op == "+":
        print("Result:", n1 + n2)
    elif op == "-":
        print("Result:", n1 - n2)
    elif op == "*":
        print("Result:", n1 * n2)
    elif op == "/":
        print("Result:", n1 / n2)
    else:
        print("Invalid operator")
except ZeroDivisionError:
    print("Error: Division by zero")
except ValueError:
    print("Error: Invalid input")

print("\n7. Using finally block")
try:
    m = 10 / 2
    print("Result:", m)
except Exception:
    print("Some error occurred")
finally:
    print("Finally block executed")

print("\n8. Try-Except-Else for division")
try:
    x = int(input("Enter numerator: "))
    y = int(input("Enter denominator: "))
    result = x / y
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Division result:", result)

print("\n9. Raising a ValueError manually")
try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative")
    print("Age:", age)
except ValueError as e:
    print("Error:", e)

print("\n10. Nested Try-Except block")
try:
    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter another number: "))
        print(a / b)
    except ZeroDivisionError:
        print("Inner except: Division by zero")
except ValueError:
    print("Outer except: Invalid input")
