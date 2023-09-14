number1 = int(input("Type a number: "))
number2 = int(input("Type another number: "))
operation = input("Type the operation (+,-,/,*): ")

if operation == "+":
    print(f"The answer is {number1 + number2}")

elif operation == "-":
    print(f"The answer is {number1 - number2}")

elif operation == "/":
    print(f"The answer is {number1//number2}")

elif operation == "*":
    print(f"The answer is {number1 * number2}")
