names = []
count = 1
stored_words = ""
while count <= 5:
    count += 1
    names.append(input("Enter a name: "))

for i in names:
    stored_words = stored_words + i + ", "

print(stored_words)