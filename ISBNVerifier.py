isbn = "1250754089"
a = []
count = -1
multiplier = 11
sum = 0
for i in isbn:
    a.append(int(i))

while count < 9:
    count += 1
    multiplier -= 1
    sum = sum + (a[count] * multiplier)

if sum % 11 == 0:
    print("It is a valid ISBN number.")

else:
    print("It is not a valid ISBN number.")