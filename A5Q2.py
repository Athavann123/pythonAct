import random
ex = ""
count = 0
while 1 != 0:
    ex = input("Press enter to roll dice. Type 'exit' to quit: ")
    count += 1
    if ex == "exit":
        break
    else:
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        print(f"Roll #{count}")
        print(f"Dice 1 = {dice1}")
        print(f"Dice 2 = {dice2}")
        print(f"Total = {dice1 + dice2}")
        print("\n")