from utilities1 import lyrics

x = lyrics.replace(",", "").replace(".", "").split()
y = []
count = -1

for i in x:
    if i not in y:
        y.append(i)

for i in y:
    count += 1
    print(f"{i} [{x.count(i)}] {x.count(i) * '*'}")