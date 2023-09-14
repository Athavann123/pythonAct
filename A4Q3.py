while 1 != 0:
    number = int(input("Enter a positive integer: "))

    if number == 0:
        break

    elif number % 2 == 0:
        print("That is an even number")

    elif number % 2 == 1:
        print("That is an odd number")