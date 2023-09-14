classmates = []
count = 1

while count <= 10:
    count += 1
    classmates.append(input("Enter a classmate: "))

search = input("Input a name to search: ")

for i in classmates:
    if i == search:
        print(f"{i} is a good friend")
        break

    else:
        print("No match")
        break