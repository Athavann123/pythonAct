fn = input("Your first name: ")
ln = input("Your last name: ")
funds = float(input("Initial funds to invest: $"))
per = float(input("Annual return percentage: "))
amount = funds + (funds * (per/100))
count = 1
print(f"Yearly return for {fn.title()} {ln.upper()}")
print(f"Initial deposit {funds:.2f}")
print(f"Year 1: {amount:.2f}")
while count < 5:
    count += 1
    amount = amount + (amount * (per/100))
    print(f"Year {count}: ${amount:.2f}")