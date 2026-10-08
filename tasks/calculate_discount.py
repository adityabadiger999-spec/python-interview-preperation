a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
opertor = input("Enter an operator (+, -, *, /, //, %, **): ")

match opertor:
    case "+":
        result = a + b
        print(f"{a} + {b} = {result}")
    case "-":
        result = a - b
        print(f"{a} - {b} = {result}")
    case "*":
        result = a * b
        print(f"{a} * {b} = {result}")
    case "/":
        if b == 0:
            print("Cannot divide by zero.")
        else:
            print(f"{a} / {b} = {a / b}")
    case "//":
        if b == 0:
            print("Cannot floor-divide by zero.")
        else:
            print(f"{a} // {b} = {a // b}")
    case "%":
        if b == 0:
            print("Cannot calculate a remainder with zero.")
        else:
            print(f"{a} % {b} = {a % b}")
    case "**":
        print(f"{a} ** {b} = {a ** b}")
    case _:
        print(f"Unsupported operator: {opertor}")