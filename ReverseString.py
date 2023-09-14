s = input("Input a string: ")
count = -1
for i in s:
    count += 1
    print(f"str{[count]} = {i.replace(' ', 'SPACE')}")

print(s[::-1].replace(" ", ""))