number = [1, 1, 2, 3, 4, 5, 5, 6, 8]

for i in number:
    if number.count(i) > 1:
        number.remove(i)

print(number)