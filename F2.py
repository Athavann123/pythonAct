s = input("Input two or more chars separated by spaces: ")
alist = s.split()
x = s.replace(" ", "")
assert len(x) >= 2, print("Must enter two or more characters!")


def swapAdjacentElements(alist):
    for i in range(1, len(alist), 2):
        alist[i], alist[i - 1] = alist[i - 1], alist[i]

    return alist


print("Initial list")
print(alist)
print(f"String version: {x}")
print("Modified list")
x = swapAdjacentElements(alist)
print(x)
s2 = ""

for i in x:
    s2 = s2 + i + ""

print(f"String version {s2}")