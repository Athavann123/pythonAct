a = "I like turtles"
b = []
c = ""
d = []
for i in a:
    b.append(i)

b.reverse()
for i in b:
    c = c + i

print(c)