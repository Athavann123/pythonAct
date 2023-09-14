def factorial(x):
    count = 0
    number = []
    total = 1

    while count < x:
        count += 1
        number.append(count)

    for i in number:
        total = total * i

    return total


while 1 != 0:
    num = int(input("Enter a positive number or 0: "))

    if num < 0:
        break

    else:
        print(f"The factorial of {num} is {factorial(num)}")

