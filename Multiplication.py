number = int(input("Enter a number between 1 and 12: "))

if number <= 0 or number > 12:
    print("Invalid number")

else:
    for i in range(13):
        print(f"{number} x {i} = {number * i}")