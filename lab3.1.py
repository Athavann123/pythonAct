print("(1) One way or (2) round trip?")
way = int(input("Enter 1 or 2: "))
print("Select age range: ")
age = int(input('''(1) Under 12
(2) 13-64
(3) 65 or older
Enter 1, 2, or 3: '''))

if way == 1 and age == 1 or age == 3:
    print(f"Total amount due $%.2f"%(1.80 * 0.5))

elif way == 1 and age == 2:
    print("Total amount is due $1.80")

elif way == 2 and age == 1 or age == 3:
    print(f"Total amount due ${3.5 * 0.5}")

elif way == 2 and age == 2:
    print(f"Total amount due $3.50")
