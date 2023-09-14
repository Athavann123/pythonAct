import math


def get_hyp(a, b):
    c = math.sqrt((a ** 2) + (b ** 2))
    print(f"The hypotenuse is {c}")


while 1 != 0:
    a = int(input("Enter 'a' value press -1 to quit: "))
    b = int(input("Enter 'b' value press -1 to quit: "))

    if a == -1 or b == -1:
        break

    else:
        get_hyp(a, b)

    print("\n")