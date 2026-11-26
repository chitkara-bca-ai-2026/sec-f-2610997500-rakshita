# Lab 16 - Solution: Modular Utility Calculator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    return a / b

def modulus(a, b):
    if b == 0:
        return None
    return a % b

def power(base, exp=2):
    return base ** exp

def format_number(n):
    # Returns an integer if the value has no decimal part, otherwise float
    if n.is_integer():
        return int(n)
    return n

def main():
    history = []
    
    while True:
        print("\n--- Utility Calculator Menu ---")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus (Remainder)")
        print("6. Power / Exponentiation")
        print("7. View Calculation History")
        print("8. Exit")
        
        choice = input("Enter your choice (1-8): ").strip()
        
        if choice == '8':
            print("Exiting program. Goodbye!")
            break
            
        elif choice == '7':
            if not history:
                print("No calculations performed yet.")
            else:
                print("\n--- Calculation History ---")
                for record in history:
                    print(record)
            continue
            
        elif choice in ('1', '2', '3', '4', '5', '6'):
            try:
                if choice == '6':
                    base_input = input("Enter base number: ").strip()
                    base = float(base_input)
                    
                    exp_input = input("Enter exponent (press Enter for default 2): ").strip()
                    if exp_input == "":
                        result = power(base)
                        record_str = f"{base} ** 2 = {format_number(result)}"
                    else:
                        exp = float(exp_input)
                        result = power(base, exp)
                        record_str = f"{base} ** {exp} = {format_number(result)}"
                else:
                    num1 = float(input("Enter first number: ").strip())
                    num2 = float(input("Enter second number: ").strip())
                    
                    if choice == '1':
                        result = add(num1, num2)
                        record_str = f"{num1} + {num2} = {format_number(result)}"
                    elif choice == '2':
                        result = subtract(num1, num2)
                        record_str = f"{num1} - {num2} = {format_number(result)}"
                    elif choice == '3':
                        result = multiply(num1, num2)
                        record_str = f"{num1} * {num2} = {format_number(result)}"
                    elif choice == '4':
                        result = divide(num1, num2)
                        if result is None:
                            print("Error: Division by zero is not allowed.")
                            continue
                        record_str = f"{num1} / {num2} = {format_number(result)}"
                    elif choice == '5':
                        result = modulus(num1, num2)
                        if result is None:
                            print("Error: Modulus by zero is not allowed.")
                            continue
                        record_str = f"{num1} % {num2} = {format_number(result)}"
                
                print(f"Result: {format_number(result)}")
                history.append(record_str)
                
            except ValueError:
                print("Invalid input! Please enter numeric values.")
        else:
            print("Invalid choice! Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()