def add(x, y): return x + y

def subtract(x, y): return x - y

def multiply(x, y): return x * y

def divide(x, y):
    if y != 0: return x / y
    else: return "Error: Division by zero"

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+ for addition, - for subtraction, * for multiplication, / for division): ")

if operation == '+': result = add(num1, num2)
elif operation == '-': result = subtract(num1, num2)
elif operation == '*': result = multiply(num1, num2)
elif operation == '/': result = divide(num1, num2)
else: 
    result = "Error: Invalid operation"
print("Result:", result)
