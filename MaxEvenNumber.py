print("Keep entering positive integer")
print("To quit, input a negative integer")
max = 0

while 1 != 0:
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        if number > max:
            max = number

    elif number == -1:
        break

print(f"Largest even number: {max}")