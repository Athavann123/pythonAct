sum = 0
count = 0
while 1 != 0:
    mark = int(input("Type a mark (Positive Integer): "))
    if mark < 0 or mark > 100:
        break
    else:
        sum = sum + mark
        count += 1

print(f"The sum is {sum}")
print(f"The average is {sum/count}")