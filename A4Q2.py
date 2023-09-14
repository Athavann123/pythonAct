password = 2019
pin_number = 0
count = -1
while pin_number != password:
    pin_number = int(input("Enter your 4-digit number: "))
    print("Incorrect pin. Access denied")
    count += 1

print("Access granted")
print(f"Number of incorrect attempts = {count}")