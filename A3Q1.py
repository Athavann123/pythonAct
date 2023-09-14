mark = int(input("Type your mark out of 100: "))

if mark >= 90 and mark <= 100:
    print("Mark is an A+")

elif mark >= 80 and mark <= 89:
    print("Mark is an A")

elif mark >= 70 and mark <= 79:
    print("Mark is a B")

elif mark >= 60 and mark <= 69:
    print("Mark is a C")

elif mark >= 50 and mark <= 59:
    print("Mark is a D")

elif mark >= 0 and mark < 50:
    print("Mark is a F")

else:
    print("Invalid mark")