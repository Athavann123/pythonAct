while 1 != 0:
    size = int(input("Enter a size between 5 and 20: "))

    if size < 5 or size > 20:
        print()

    else:
        count = -1
        next_counter = size
        while count <= (size - 2):
            count += 1
            print((count * "-") + "\\")

        print((size * "-") + "|")

        while next_counter > 0:
            next_counter -= 1
            print((next_counter * "-") + "/")
        break
