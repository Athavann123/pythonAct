number = int(input("How many students: "))
count = 1
aa = 0
a = 0
b = 0
c = 0
d = 0
f = 0

while count <= number:
    count += 1
    marks = int(input("Input mark: "))

    if marks >= 90 and marks <= 100:
        aa += 1

    elif marks >= 80 and marks <= 89:
        a += 1

    elif marks >= 70 and marks <= 79:
        b += 1

    elif marks >= 60 and marks <= 69:
        c += 1

    elif marks >= 50 and marks <= 59:
        d += 1

    elif marks < 50 and marks >= 0:
        f += 1

    elif marks < 0 or marks > 100:
        print("Invalid Mark")
        count -= 1

print("Mark (as a percentage) Letter Grade Number of students")
print(f"          90-100             A+            {aa}")
print(f"           80-89             A            {a}")
print(f"           70-79             B            {b}")
print(f"           60-69             C            {c}")
print(f"           50-59             D            {d}")
print(f"    Less than 50             F            {f}")