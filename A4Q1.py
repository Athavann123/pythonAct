number = int(input("Type a positive integer: "))

for i in range(number):
    i += 1
    print(f"{i}\t{i ** 2}\t{i ** 3}")