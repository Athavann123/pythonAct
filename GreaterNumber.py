number1 = int(input("Type a number: "))
number2 = int(input("Type the second number: "))
number3 = int(input("Type the third number: "))

if number1 > number2 and number1 > number3:
    print(f"The greatest number is {number1}")

elif number2 > number1 and number2 > number3:
    print(f"The greatest number is {number2}")

else:
    print(f"The greatest number is {number3}")