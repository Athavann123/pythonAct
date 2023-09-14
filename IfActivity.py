good_credit = False
house_price = 1000000
down_payment = 0
if good_credit:
    print("You need to put down 10%")
    down_payment = house_price * 0.1

else:
    print("You need to put down 20%")
    down_payment = house_price * 0.2

print(f"Down payment is ${down_payment}")

