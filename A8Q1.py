import random


def rollDice(number):
    sum = 0
    count = 1
    while count <= number:
        count += 1
        dice = random.randint(1, 6)
        sum = sum + dice
        print(f"Dice {count} = {dice}")

    print(f"Sum = {sum}")


while 1 != 0:
    num = int(input("How much dice do you want to roll: "))

    if num == 0:
        break

    else:
        rollDice(num)