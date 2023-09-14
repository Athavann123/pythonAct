number1 = [1, 2, 3, 4, 5]
number2 = [5, 4, 3, 2, 1]

number1.sort()
number2.sort()

for i in range(len(number1)):
    if number1[i] != number2[i]:
        print("Different")
        break

    else:
        print("Same")
        break