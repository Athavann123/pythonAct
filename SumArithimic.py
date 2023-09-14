def sum(upperbound):
    half = (1 + upperbound) / 2
    sn = upperbound * half
    print(f"The sum is {sn}")


while 1 != 0:
    upperbound = int(input("Enter an upperbound value: "))

    if upperbound == 0:
        break

    else:
        sum(upperbound)