count = 1
sum = 0
marks = []
while count <= 10:
    count += 1
    marks.append(int(input("Enter a mark: ")))

for i in marks:
    sum = sum + i

print(f"The sum is {sum}")
print(f"The average is {sum/(count-1)}")