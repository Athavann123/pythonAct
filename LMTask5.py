import random


def generateDNASequence():
    a = "TGCA"
    y = ""
    count = 0
    while count < 40:
        count += 1
        x = random.randint(0, 3)
        y = y + a[x]

    return y

def applyGammaRadiation(str1):
    z = [char for char in str1]
    a = "TGCA"
    r1 = random.randint(0, 39)
    r2 = random.randint(0, 3)
    p = random.randint(1, 2)

    if p == 2:
        z[r1] = a[r2]
        s = "".join(z)
        return s

    elif p == 1:
        return str1


def detectMutation(str1, str2):
    count = -1
    c = 0
    y = " "
    x = "^"
    while count < 39:
        count += 1

        if str1[count] == str2[count]:
            c += 1

        else:
            break

    print((y * c) + x)


x = generateDNASequence()
print(x)
y = applyGammaRadiation(x)
print(y)

if x == y:
    print("Same")

else:
    detectMutation(x, y)