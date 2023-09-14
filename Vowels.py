vowels = ["a", "e", "i", "o", "u"]
b = []
a = ""

while 1 != 0:
    ex = input("Enter a word: ")

    for i in ex:
        b.append(i)

    if ex == "exit":
        break

    else:
        for i in vowels:
            if ex.count(i) > 0:
               a = ex.replace(i, "")

            if ex.count(i.upper()) > 0:
                a = ex.replace(i.upper(), "")

        print(a)