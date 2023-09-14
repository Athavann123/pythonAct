import math


def slope(y2, y1, x2, x1):
    s = (y2 - y1)/(x2-x1)
    print(f"The slope is {s}")


def length(x2, x1, y2, y1):
    inside_root = ((x2 - x1) ** 2 + (y2 - y1) ** 2)
    root = math.sqrt(inside_root)
    print(f"The length is {root}")


def midpoint(x1, x2, y1, y2):
    x = (x1 + x2)/2
    y = (y1 + y2)/2
    print(f"The midpoint is {x},{y}")


def quadratic_formula(a, b, c):
    discri = (b ** 2) - (4 * a * c)
    if discri < 0:
        print("No x-intercepts")

    else:
        root = math.sqrt(discri)
        x1 = ((-1) * (b) + root)/(2 * a)
        x2 = ((-1) * (b) - root)/(2 * a)
        print(f"X1 = {x1} and X2 = {x2}")


while 1 != 0:
    print("0: Exit")
    print("1: Slope")
    print("2: Length of a line")
    print("3: Midpoint of a line")
    print("4: Quadratic Formula")
    option = int(input("What calculation do you want to do press (1, 2, 3, 4): "))

    if option == 0:
        break

    if option == 1:
        y2 = int(input("Type y2 value: "))
        y1 = int(input("Type y1 value: "))
        x2 = int(input("Type x2 value: "))
        x1 = int(input("Type x1 value: "))
        slope(y2, y1, x2, x1)

    elif option == 2:
        lx2 = int(input("Enter x2 value: "))
        lx1 = int(input("Enter x1 value: "))
        ly2 = int(input("Enter y2 value: "))
        ly1 = int(input("Enter y1 value: "))
        length(lx2, lx1, ly2, ly1)

    elif option == 3:
        mx1 = int(input("Enter x1 value: "))
        mx2 = int(input("Enter x1 value: "))
        my1 = int(input("Enter y1 value: "))
        my2 = int(input("Enter y2 value: "))
        midpoint(mx1, mx2, my1, my2)

    elif option == 4:
        a = int(input("Enter a value: "))
        b = int(input("Enter b value: "))
        c = int(input("Enter c value: "))
        quadratic_formula(a, b, c)

    print("\n")