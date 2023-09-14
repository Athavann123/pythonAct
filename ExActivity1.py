import random
numbers = []
count = 1
user = ""
while count <= 50:
    count += 1
    numbers.append(random.randint(0, 9))

for i in numbers:
    print(i)

print("\n")

try:
    user = int(input("Enter an input between 1-10: "))

except ValueError:
    print("Not a number")
    exit()

for i in numbers:
    try:
        print(user//i)

    except ZeroDivisionError:
        print("Undefined")
