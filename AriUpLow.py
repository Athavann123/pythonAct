def sum(lowerbound, upperbound):

    n = (upperbound - lowerbound) + 1
    half = (lowerbound + upperbound) / 2
    print(f"The sum is {n * half}")


while 1 != 0:
    lowerbound = int(input("Enter lowerbound value: "))
    upperbound = int(input("Enter upperbound value: "))

    if lowerbound == 0 or upperbound == 0:
        break

    else:
        sum(lowerbound, upperbound)