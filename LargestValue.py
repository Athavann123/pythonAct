count = 1
number = []
max_number = 0

while count <= 15:
    count += 1
    number.append(int(input("Enter a number: ")))

for i in number:
    if max_number < i:
        max_number = i

print(f"The largest number is {max_number}")