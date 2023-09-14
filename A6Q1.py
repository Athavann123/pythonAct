import random
ex = ""
count = 0
while 1 != 0:
    count += 1
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice3 = random.randint(1, 6)
    dice4 = random.randint(1, 6)
    dice5 = random.randint(1, 6)
    roll = int(input("How many dice would you like to roll between 1-5. Press -1 to exit: "))

    if roll == -1:
        break

    elif roll == 1:
        print(f"Sum: {dice1}")

    elif roll == 2:
        print(f"Sum: {dice1 + dice2}")

    elif roll == 3:
        print(f"Sum: {dice1 + dice2 + dice3}")

    elif roll == 4:
        print(f"Sum: {dice1 + dice2 + dice3 + dice4}")

    elif roll == 5:
        print(f"Sum: {dice1 + dice2 + dice3 + dice4 + dice5}")

    print("\n")