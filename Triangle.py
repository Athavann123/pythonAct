while 1 != 0:
    s = int(input("Enter size between 5 and 20: "))
    count = s

    if s < 5 or s > 20:
        pass

    else:
        for i in range(s):
            print("-" * i + "\\")

        print("-" * s + "|")

        while count > 0:
            count -= 1
            print("-" * count + "/")