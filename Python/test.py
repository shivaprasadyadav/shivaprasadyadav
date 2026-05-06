# Simple Python Test Program

def greet(name):
    return f"Hello, {name}! Welcome to Python 🚀"

def calculate(a, b):
    return a + b, a - b, a * b, a / b if b != 0 else "Cannot divide by zero"

def main():
    print("=== Python Test Program ===")

    # Take user input
    name = input("Enter your name: ")
    print(greet(name))

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        add, sub, mul, div = calculate(num1, num2)

        print("\n--- Results ---")
        print(f"Addition: {add}")
        print(f"Subtraction: {sub}")
        print(f"Multiplication: {mul}")
        print(f"Division: {div}")

    except ValueError:
        print("Invalid input! Please enter numbers only.")

    # Loop test
    print("\nCounting from 1 to 5:")
    for i in range(1, 6):
        print(i)

if __name__ == "__main__":
    main()