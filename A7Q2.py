import random
count = 1
number = []

while count <= 50:
    count += 1
    number.append(random.randint(1, 100))

for i in number:
    print(i)

print("\n")

num = int(input("Type in a number: "))

for i in number:
    if i % num == 0:
        print(f"{i} is divisible by {num}")
