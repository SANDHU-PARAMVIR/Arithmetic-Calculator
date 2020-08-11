# Arithmetic Calculator
# Param Sandhu - 301118847


def menu():
    print("\nHello User")
    print("1. ADD")
    print("2. SUBTRACT")
    print("3. MULTIPLY")
    print("4. DIVIDE")
    print("5. EXIT")
    pick = int(input("Enter a Choice: "))
    return pick


def main():
    choice = menu()
    while choice != 5:
        if choice == 1:
            # adds two numbers
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            print(num1, "+",  num2, "=", num1 + num2)
        elif choice == 2:
            # subtracts two numbers
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            print(num1, "-",  num2, "=", num1 - num2)
        elif choice == 3:
            # multiplies two numbers
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            print(num1, "*",  num2, "=", num1 * num2)
        elif choice == 4:
            # divides two numbers
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            print(num1, "/",  num2, "=", num1 / num2)
        else:
            print("Invalid Entry")
        choice = menu()


main()
