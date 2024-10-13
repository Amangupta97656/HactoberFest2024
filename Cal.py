import operator

# Function to perform calculations without using operators
def calculate(num1, num2, operation):
    ops = {
        'add': operator.add,
        'subtract': operator.sub,
        'multiply': operator.mul,
        'divide': operator.truediv
    }

    if operation in ops:
        result = ops[operation](num1, num2)
        return result
    else:
        return "Invalid operation"

# Main program
def main():
    print("Simple Calculator without using operators")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Choose operation: add, subtract, multiply, divide")
    operation = input("Enter operation: ").lower()
    
    result = calculate(num1, num2, operation)
    
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
