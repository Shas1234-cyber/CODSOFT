def simple_calculator():
    print("----------------")
    print("SIMPLE CALCULATOR")
    print("----------------")
    
    # Get users input
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        return
    
    print("\nSelect operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (^)")
    print("6. Modulus (%)")
    
    try:
        choice = input("Enter operation choice (1-6): ")
        
        if choice == '1':
            result = num1 + num2
            print(f"\nResult: {num1} + {num2} = {result}")
        elif choice == '2':
            result = num1 - num2
            print(f"\nResult: {num1} - {num2} = {result}")
        elif choice == '3':
            result = num1 * num2
            print(f"\nResult: {num1} * {num2} = {result}")
        elif choice == '4':
            if num2 == 0:
                print("\nError! Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"\nResult: {num1} / {num2} = {result}")
        elif choice == '5':
            result = num1 ** num2
            print(f"\nResult: {num1} ^ {num2} = {result}")
        elif choice == '6':
            if num2 == 0:
                print("\nError! Modulus by zero is not allowed.")
            else:
                result = num1 % num2
                print(f"\nResult: {num1} % {num2} = {result}")
        else:
            print("\nInvalid choice! Please select 1-6.")
    except:
        print("\nAn error occurred during calculation.")

# Run the calculator
while True:
    simple_calculator()
    again = input("\nCalculate again? (y/n): ").lower()
    if again != 'y':
        print("\nGoodbye!")
        break