##############################
# Lab3  --- Starting code (you can cut-and-paste into pycharm)
# Author name: Athavann Thulasiranjan
# Student ID: 218658419
# Email address: athava08@my.yorku.ca
# Section B

# Code for task 1 after this line
print("\n--- Task 1 ---: Compute Fare")
print("(1) One way or (2) round trip?")
way = int(input("Enter 1 or 2: "))
print("Select age range: ")
age = int(input('''(1) Under 12
(2) 13-64
(3) 65 or older
Enter 1, 2, or 3: '''))

if way == 1 and age == 1 or age == 3:
    print("Total amount due $%.2f [One way (reduced fare)]"%(1.80 * 0.5))

elif way == 1 and age == 2:
    print("Total amount is due $1.80 [One way (Full fare)]")

elif way == 2 and age == 1 or age == 3:
    print(f"Total amount due ${3.5 * 0.5} [round trip (reduced fare)]")

elif way == 2 and age == 2:
    print("Total amount due $3.50 [round trip (full fare)]")


# Code for task 2 after this line
print("\n--- Task 2 ---: Parse string")
a = input("Input a string: ")
count = -1
b = a.replace(" ", "")
x = ""

for i in a:
    count += 1
    x = i
    print(f"str[{count}] = {x.replace(' ', 'SPACE')}")

print("Reverse no spaces: " + b[::-1])

# Code for task 3 after this line
print("\n--- Task 3 ---: The maximum *even* number")
stored_number = 0

while 1 != 0:
    number = int(input("Enter a number: "))

    if number == -1:
        break

    if number > stored_number and number % 2 == 0:
        stored_number = number

print(f"Largest even number: {stored_number}")

# Code for task 4 after this line
print("\n--- Task 4 ---: Better triangle draw")
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


input("Press enter to quit.")
