####
# EECS1015 - Midterm
# Name: Athavann Thualasiranjan
# Student ID: 218658419
# Email: athava08@my.yorku.ca
#
##

def task0():
  pass

def task1():
  pass

def task2():
  pass

def task3():
  pass

def task4():
  pass


# main function for EECS1015 midterm
def main():
    task0()
    print("\n-- TASK 1 --\n")
    print('''Midterm Exam - EECS1015
Name: Athavann Thulasiranjan
Student ID: 218658419
email: athava08@my.yorku.ca
    ''')
    task1()
    print("\n-- Task 2 --\n")
    fn = input("First Name: ")
    ln = input("Last Name: ")
    hr = int(input("How many hours do you work a week: "))
    hw = float(input("What is your hourly wage: "))
    gross = hr * hw * 4
    tax = gross * 0.25
    sal = gross-tax
    print(f'''Employee: {ln}, {fn}
${gross:.2f} Monthly salary (gross)
$-{tax:.2f} 25% Tax deduction
${sal:.2f} Monthly salary (net)
''')
    task2()
    print("\n-- Task 3 --\n")
    cash = 10
    while 1 != 0:
        item = int(input(f'''You have {cash:.2f} - what item do you want?
    1: Falafel $3.00
    2: Pizza   $6.00
    3: Salad   $1.50
    4: Coffee  $1.00
    Enter 0 to exit.
    Your order: '''))

        if item == 1:
            print("Order for *falafel* confirmed.")
            cash = cash - 3.00

        elif item == 2:
            print("Order for *pizza* confirmed.")
            cash = cash - 6.00

        elif item == 3:
            print("Order for *salad* confirmed.")
            cash = cash - 1.50

        elif item == 4:
            print("Order for *coffee* confirmed.")
            cash = cash - 1.00

        if cash == 0 or item == 0:
            print("Thank you!")
            break

        if cash < 0:
            print("Sorry, you don't have enough money for that item.")
            break

        if item < 0 or item > 4:
            pass
    task3()
    print("\n-- Task 4 --\n")
    import random

    def sim():
        c = 0
        count = 0
        print("Rolling dice 10 times . . .")
        while c < 10:
            c += 1
            dice = random.randint(1, 6)
            x = f"[{dice}]"

            if dice == 6:
                x = f"*{x}*"
                count += 1

            print(x)

        if count >= 2:
            print("YOU WIN!")

        else:
            print("YOU LOSE!")

    sim()
    while 1 != 0:
        command = input("Do you want to play again? (Y/N):")
        if command == "N":
            break

        else:
            sim()
    task4()
    print("\n-- Task 4 --\n")

    def generateDNASequence():
        a = "TGCA"
        y = ""
        count = 0
        while count < 40:
            count += 1
            x = random.randint(0, 3)
            y = y + a[x]

        return y

    def applyGammaRadiation(str1):
        z = [char for char in str1]
        a = "TGCA"
        r1 = random.randint(0, 39)
        r2 = random.randint(0, 3)
        p = random.randint(1, 2)

        if p == 2:
            z[r1] = a[r2]
            s = "".join(z)
            return s

        elif p == 1:
            return str1

    def detectMutation(str1, str2):
        count = -1
        c = 0
        y = " "
        x = "^"
        while count < 39:
            count += 1

            if str1[count] == str2[count]:
                c += 1

            else:
                break

        print((y * c) + x)

    x = generateDNASequence()
    print(x)
    y = applyGammaRadiation(x)
    print(y)

    if x == y:
        print("Same")

    else:
        detectMutation(x, y)


if __name__=="__main__":
    main()
