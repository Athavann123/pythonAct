import random

dice = 0
count = 0
total = 0
while 1 != 0:
    print("Dice Game")
    print("Rolling Die 10 times")

    for i in range(10):
        dice = random.randint(1, 6)
        print(f"Roll {i+1}: [{dice}]")
        total = total + dice

        if dice == 1:
            count += 1

    if count == 2:
        total = total + 10
        print("+10 Bonus for snake eyes [1][1]!")

    if total > 35:
        print(f"Total {total} -- OVER 35 POINTS [YOU WIN!]")

    elif total < 35:
        print(f"Total {total} -- TOO FEW POINTS [YOU LOSE!]")

    elif total < 35:
        print(f"Total {total} -- TOO FEW POINTS [YOU LOSE!]")

    print(count)

    c = input("Enter 'Y' to play again: ")

    if c == "Y" or c == "y":
        total = total - total
        count = 0

    else:
        break
