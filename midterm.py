####
# EECS1015 - Midterm
# Name: Athavann Thulasiranjan
# Student ID: 218658419
# Email: athava08@my.yorku.ca
# Section B
##


def task0():
    print("Midterm Exam - EECS1015")
    print("Name: Athavann Thulasiranjan")
    print("Student ID: 218658419")
    print("email: athava08@my.yorku.ca")
    print("Section B")

def task1():
    fn = input("Your first name: ")
    ln = input("Your last name: ")
    funds = float(input("Initial funds to invest: $"))
    per = float(input("Annual return percentage: "))
    amount = funds + (funds * (per / 100))
    count = 1
    print(f"Yearly return for {fn.title()} {ln.upper()}")
    print(f"Initial deposit {funds:.2f}")
    print(f"Year 1: {amount:.2f}")
    while count < 5:
        count += 1
        amount = amount + (amount * (per / 100))
        print(f"Year {count}: ${amount:.2f}")

def task2():
    print("Soda Vending Machine")
    cost = 0
    while 1 != 0:
        print(f"Current amount ${cost:.2f} out of $1.00")
        print("1. Toonie ($2.00)")
        print("2. Loonie ($1.00)")
        print("3. Quarter ($0.25)")
        print("4. Dime ($0.10)")
        print("5. Nickel ($0.05)")
        s = int(input("Selection [1-5]? "))

        if s == 1:
            cost = cost + 2.00

        elif s == 2:
            cost = cost + 1.00

        elif s == 3:
            cost = cost + 0.25

        elif s == 4:
            cost = cost + 0.10

        elif s == 5:
            cost = cost + 0.05

        elif s < 1 or s > 5:
            print("Invalid selection!")

        if cost == 1:
            print("Total amount provided: $1.00")
            print("Thank you for your purchase.")
            break

        if cost > 1:
            print(f"Total amount provided: ${cost:.2f}")
            print("Thank you for your purchase.")
            print(f"Please take your change ${(cost - 1):.2f}")
            break


def task3():
    import random

    dice = 0
    count = 0
    total = 0
    while 1 != 0:
        print("Dice Game")
        print("Rolling Die 10 times")

        for i in range(10):
            dice = random.randint(1, 6)
            print(f"Roll {i + 1}: [{dice}]")
            total = total + dice

            if dice == 1:
                count += 1

        if count == 2:
            total = total + 10
            print("+10 Bonus for snake eyes [1][1]!")

        if total > 35:
            print(f"Total {total} -- OVER 35 POINTS [YOU WIN!]")

        elif total < 35:
            print(f"Total {total} -- TOO FEW POINTS [YOU LOSE!]")

        elif total < 35:
            print(f"Total {total} -- TOO FEW POINTS [YOU LOSE!]")

        c = input("Enter 'Y' to play again: ")

        if c == "Y" or c == "y":
            total = total - total
            count = 0

        else:
            break


def task4():
    s = input("Enter string with one word with \"quotes\": ")

    def countCases(s):
        uc = 0
        lc = 0

        for i in s:
            if i.isupper():
                uc += 1

            if i.islower():
                lc += 1

        print(f"This string has {uc} uppercase characters.")
        print(f"This string has {lc} lowercase characters.")

    def flipCase(st):
        return st.swapcase()

    def cutQuotedText(st):
        d = st[::-1]
        b = st.split()
        c = 0
        e = 0
        for i in st:
            c = st.find("\"")

        for i in d:
            e = d.find("\"")

        if c == -1 or e == -1:
            return "'ERROR! No quoted text.'"

        else:
            return f'Quote removed: \'{st.replace(st[c:-e], "")}\''

    countCases(s)
    print(flipCase(s))
    print(cutQuotedText(s))

# main function for EECS1015 midterm
def main():
    print("\n")
    task0()
    print("\n----------Task 1-----------")
    task1()
    print("\n----------Task 2-----------")
    task2()
    print("\n----------Task 3-----------")
    task3()
    print("\n----------Task 4-----------")
    task4()
    input("\nPress enter to exit.")

if __name__=="__main__":
    main()
