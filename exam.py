def compountinterest(p, r, n):
    print("Years Future Value")
    count = 0
    while count < n:
        count += 1
        rate = r / 100
        half = (1 + rate) ** count
        a = p * half
        print(f"{count}      {round(a, 3)}")


while 1 != 0:
    ex = input("Press enter to calculate interest, type 'exit' to quit: ")

    if ex == "exit":
        break

    else:
        p = int(input("Input the principle amount: "))
        r = int(input("Input the interest rate as a percentage: "))
        t = int(input("Input the number of years: "))
        compountinterest(p, r, t)