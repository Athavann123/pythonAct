print("Soda Vending Machine")
cost = 0
while 1 != 0:
    print(f"Current amount ${cost:.2f} out of $1.00")
    print("1. Toonie ($2.00)")
    print("2. Loonie ($1.00)")
    print("3. Quarter ($0.25)")
    print("4. Dime ($0.10)")
    print("5. Nickel ($0.05)")
    s = int(input("Selection [1-5]? "))

    if s == 1:
        cost = cost + 2.00

    elif s == 2:
        cost = cost + 1.00

    elif s == 3:
        cost = cost + 0.25

    elif s == 4:
        cost = cost + 0.10

    elif s == 5:
        cost = cost + 0.05

    elif s < 1 or s > 5:
        print("Invalid selection!")

    if cost == 1:
        print("Total amount provided: $1.00")
        print("Thank you for your purchase.")
        break

    if cost > 1:
        print(f"Total amount provided: ${cost:.2f}")
        print("Thank you for your purchase.")
        print(f"Please take your change ${(cost-1):.2f}")
        break
