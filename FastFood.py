price = 0

while 1 != 0:
    print("-1: Exit")
    print("1: Hamburger, $7.00")
    print("2: Fries, $2.00")
    print("3: Onion Rings, $ 3.00")
    print("4: Soda, $1.00")
    print("5: Poutine, $4.50")
    print("6: Chicken Sandwich $8.00")
    order = int(input("What do you want to order, press from 1 - 6: "))
    print("\n")

    if order == -1:
        break

    elif order == 1:
        price = price + 7.00

    elif order == 2:
        price += 2.00

    elif order == 3:
        price += 3.00

    elif order == 4:
        price += 1.00

    elif order == 5:
        price += 4.50

    elif order == 6:
        price += 8.00

print(f"The price of your order is ${price}0")