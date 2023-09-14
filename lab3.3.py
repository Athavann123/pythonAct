stored_number = 0

while 1 != 0:
    number = int(input("Enter a number: "))

    if number == -1:
        break

    if number > stored_number and number % 2 == 0:
        stored_number = number

print(f"Largest even number: {stored_number}")