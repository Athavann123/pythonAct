from utilities1 import raster
from math import sqrt

while 1 != 0:
    r = int(input("Radius [1 to 9]: "))

    for i in range(19):
        for j in range(19):
            x = i - 10
            y = j - 10

            if sqrt((x**2)+(y**2)) <= r:
                raster[i][j] = "*"

            else:
                raster[i][j] = ' '

    for i in range(19):
        for j in range(19):
            print(raster[i][j], end='')

        print("\n")

    com = input("Try again: Y/N? ")

    if com.upper() == "N":
        break
