number = int(input("Type a number greater than zero: "))
count = 1
while count <= number:
    print(count)
    count = count + 1

    if count % 2 == 1:
        count = count + 1


