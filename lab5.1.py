import random

def generateRandomList(list_size, maximum_integer_value):
    a = []

    for i in range(list_size):
        a.append(random.randint(0, maximum_integer_value))

    return a


def computeAverage(l):
    total = 0
    for i in l:
        total = total + i

    average = total/len(l)
    return average


size = int(input("Input list size: "))
max = int(input("Input max int: "))
a = generateRandomList(size, max)
average = computeAverage(a)
print("Generated list")
print(a)
print(f"Average value = {average:.4f}")