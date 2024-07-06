def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def modulo(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x % y

print("Simple Calculator")
print("Operations:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulo")

while True:
    choice = input("Enter operation number (1-5): ")
    if choice in ('1', '2', '3', '4', '5'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
        elif choice == '5':
            print("Result:", modulo(num1, num2))
        
        again = input("Do you want to perform another calculation? (yes/no): ")
        if again.lower() != 'yes':
            break
    else:
        print("Invalid input. Please enter a number between 1 and 5.")
