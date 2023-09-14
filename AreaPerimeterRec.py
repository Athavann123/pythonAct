import AreaPeriRect

rect = AreaPeriRect.Rectangle()

while 1 != 0:
    l = int(input("Enter length: "))
    w = int(input("Enter width: "))

    if l == 0 or w == 0:
        break

    else:
        rect.perimeter(l, w)
        rect.area(l, w)

    print("\n")