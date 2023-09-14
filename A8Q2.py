def printRect(l , w, c):
    for i in range(w):
        for j in range(l):
            print(f"{c}", end=" ")

        print()


l = int(input("Enter length: "))
w = int(input("Enter width: "))
c = input("Enter character: ")

printRect(l, w, c)