age = int(input("What is your age: "))
student = input("Are you a student (Y/N)?: ")

if age <= 12:
    print("Fare type 'CHILD' - price: $ 0.50")

elif student == "Y":
    print("Fare Type 'STUDENT' - Price: $1.00")

elif age >= 65:
    print("Fare Type 'SENIOR' - Price: $0.50")

else:
    print("Fare Type 'ADULT' - Price: $1.50")