from StudentClass import Student

stu = Student()
while 1 != 0:
    print("0: Exit")
    print("1: Add student's name")
    print("2: Get student's name")
    print("3: Add test mark")
    print("4: Get test mark")
    print("5: Get average")
    print("6: Get high mark")
    print("7: Print info")
    option = int(input("Enter a number based on menu (1-7): "))

    if option == 0:
        break

    if option == 1:
        name = input("Enter name: ")
        nm = stu.add_student(name)

    if option == 2:
        get = stu.get_student()
        print(f"The student name is {get}")

    if option == 3:
        test = int(input("What test from 1-3 are you going to input the mark in: "))
        mark = int(input("What is the test mark: "))
        test_mark = stu.add_mark(test, mark)

    if option == 4:
        tes = int(input("What test do you want to see: "))
        stu.get_mark(tes)

    if option == 5:
        stu.get_average()

    if option == 6:
        stu.get_highmark()

    if option == 7:
        stu.print_info()

    print("\n")