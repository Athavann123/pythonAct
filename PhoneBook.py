names = []
phone_numbers = []
count = 1
while count <= 10:
    count += 1
    names.append(input("Enter a name: "))
    phone_numbers.append(int(input("Enter the phone number for that person: ")))

search = input("Search a name: ")

for i in range(len(names)):
    if search == names[i]:
        print(f"{names[i], phone_numbers[i]}")
        break
