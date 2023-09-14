cash = 10
while 1 != 0:
    item = int(input(f'''You have {cash:.2f} - what item do you want?
1: Falafel $3.00
2: Pizza   $6.00
3: Salad   $1.50
4: Coffee  $1.00
Enter 0 to exit.
Your order: '''))

    if item == 1:
        print("Order for *falafel* confirmed.")
        cash = cash - 3.00

    elif item == 2:
        print("Order for *pizza* confirmed.")
        cash = cash - 6.00

    elif item == 3:
        print("Order for *salad* confirmed.")
        cash = cash - 1.50

    elif item == 4:
        print("Order for *coffee* confirmed.")
        cash = cash - 1.00

    if cash == 0 or item == 0:
        print("Thank you!")
        break

    if cash < 0:
        print("Sorry, you don't have enough money for that item.")
        break

    if item < 0 or item > 4:
        pass