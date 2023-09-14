#########################
# EECS1015 - Lab 5
# Athavann Thulasiranjan
# 218658419
# athava08@my.yorku.ca
# Your Section: B
#########################

import random


def main():
    def task1():
        def generateRandomList(list_size, maximum_integer_value):
            a = []

            for i in range(list_size):
                a.append(random.randint(0, maximum_integer_value))

            return a

        def computeAverage(l):
            total = 0
            for i in l:
                total = total + i

            average = total / len(l)
            return average

        size = int(input("Input list size: "))
        max = int(input("Input max int: "))
        a = generateRandomList(size, max)
        average = computeAverage(a)
        print("Generated list")
        print(a)
        print(f"Average value = {average:.4f}")
    print("\n--------- TASK 1: Random List -------------")
    task1()
    print("\n--------- TASK 2: Phone number to text ---")
    def task2():
        def stringToCharLst(inputString):
            a = list(inputString)
            return a

        def charsToWord(alist):
            c = []
            valueassociation = {
                '0': 'zero',
                '1': 'one',
                '2': 'two',
                '3': 'three',
                '4': 'four',
                '5': 'five',
                '6': 'six',
                '7': 'seven',
                '8': 'eight',
                '9': 'nine',
                '-': 'dash'
            }

            for i in alist:
                c.append(valueassociation.get(i))

            return c

        b = ""
        print("Enter phone number as XXX-XXX-XXXX")
        number = input("Type here: ")
        x = stringToCharLst(number)
        y = charsToWord(x)
        print(x)
        print(y)

        for i in range(len(y)):
            b = b + "- >" + y[i]

        print(b)
    task2()

    input("Press enter to exit.")


if __name__ == "__main__":
    main()
