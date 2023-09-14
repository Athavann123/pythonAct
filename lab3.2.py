a = input("Input a string: ")
count = -1
b = a.replace(" ", "")
x = ""

for i in a:
    count += 1
    x = i
    print(f"str[{count}] = {x.replace(' ', 'SPACE')}")

print("Reverse no spaces: " + b[::-1])
