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