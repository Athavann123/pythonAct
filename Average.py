number = int(input("How many numbers are being added? "))
sum = 0

if number <= 0:
    print("Invalid number")
    exit()

else:
    for i in range(number):
        marks = int(input("Enter a mark: "))
        sum += marks

average = sum/number
print(f"Your sum is {sum}")
print(f"Your average is {average}")