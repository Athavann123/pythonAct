###########################################
# EECS1015 - Final exam (final.py)
# Name: Athavann Thulasiranjan
# Student ID: 218658419
# Email: athava08@my.yorku.ca
# Section B
###########################################

# import the approriate items from utilities.py and other modules may you require
import random, time
from utilities import students, studentsInfo, SeaLife

def task0():
    print('''
    Final Exam - EECS1015
    Name: Athavann Thulasiranjan
    Student ID: 218658419
    email: athava08@my.yorku.ca
    Section B
    ''')


def task1():
    print("Rock, Paper, Scissors!")
    while 1 != 0:
        print("Make your selection. . .")
        rps = {1: "rock", 2: "paper", 3: "scissors"}
        p1 = int(input("(1) rock, (2) paper, (3) scissors? "))
        p2 = random.randint(1, 3)

        if p1 < 1 or p1 > 3:
            print("Invalid selection. Try again.")

        else:
            print(f"You: {rps[p1]}")
            print(f"HAL: {rps[p2]}")
            if p1 == 1 and p2 == 3:
                print(f"You win")

            elif p1 == 2 and p2 == 1:
                print(f"You win")

            elif p1 == 3 and p2 == 2:
                print(f"You win")

            elif p1 == 1 and p2 == 2:
                print(f"HAL wins")

            elif p1 == 2 and p2 == 3:
                print(f"HAL wins")

            elif p1 == 3 and p2 == 1:
                print(f"HAL wins")

            else:
                print("A tie")

            cmd = input("Play again (Y/N)? ")

            if cmd.upper() == "N":
                break

            else:
                pass

            print("\n")

def task2():
    s = input("Input two or more chars separated by spaces: ")
    alist = s.split()
    x = s.replace(" ", "")
    assert len(x) >= 2, print("Must enter two or more characters!")

    def swapAdjacentElements(alist):
        for i in range(1, len(alist), 2):
            alist[i], alist[i - 1] = alist[i - 1], alist[i]

        return alist

    print("Initial list")
    print(alist)
    print(f"String version: {x}")
    print("Modified list")
    x = swapAdjacentElements(alist)
    print(x)
    s2 = ""

    for i in x:
        s2 = s2 + i + ""

    print(f"String version {s2}")


def task3():
    def check(alist, index):
        for i in alist:
            if i == index:
                return True

        return False

    finaldict = {}

    for i in range(len(students)):
        year = ""

        if check(studentsInfo['Year 1'], i):
            year = "Year 1"

        elif check(studentsInfo['Year 2'], i):
            year = "Year 2"

        elif check(studentsInfo['Year 3'], i):
            year = "Year 3"

        elif check(studentsInfo['Year 4'], i):
            year = "Year 4"

        program = ""

        if check(studentsInfo['CS'], i):
            program = "CS"

        elif check(studentsInfo['DM'], i):
            program = "DM"

        elif check(studentsInfo['BZ'], i):
            program = "BZ"

        elif check(studentsInfo['SE'], i):
            program = "SE"

        housing = ""

        if check(studentsInfo['On Campus'], i):
            housing = "On Campus"

        if check(studentsInfo['Off Campus'], i):
            housing = "Off Campus"

        finaldict[students[i]] = "{0:>10} ({1}) Program: {2} Housing: {3}".format(students[i], year, program, housing)

    for i in sorted(finaldict):
        print(finaldict[i])

def task4():
    com = input("Press enter to start aquarium...")
    timestep = 0
    s1 = SeaLife(random.randint(0, 1), random.randint(5, 30))
    s2 = SeaLife(random.randint(0, 1), random.randint(5, 30))
    s3 = SeaLife(random.randint(0, 1), random.randint(5, 30))
    s4 = SeaLife(random.randint(0, 1), random.randint(5, 30))
    s5 = SeaLife(random.randint(0, 1), random.randint(5, 30))
    while 1 != 0:
        timestep += 1
        print(40 * "-" + f"Time: {timestep}")
        print(s1.getStr())
        s1.move()
        print(s2.getStr())
        s2.move()
        print(s3.getStr())
        s3.move()
        print(s4.getStr())
        s4.move()
        print(s5.getStr())
        s5.move()
        time.sleep(0.3)

        if timestep == 50:
            break

def main():
    print("\n--------- Task0: Submission Info       ------------")
    task0()
    print("\n--------- Task1: Rock, Paper, Scissors ------------")
    task1()
    print("\n--------- Task2: Swap List Elements    ------------")
    task2()
    print("\n--------- Task3: Student Info          ------------")
    task3()
    print("\n--------- Task4: Aquarium              ------------")
    task4()

    input("Press enter to quit.")


if __name__ == "__main__":
    main()
