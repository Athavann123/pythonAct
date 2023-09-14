import random
c = 0
count = 0
print("Rolling dice 10 times . . .")
while c < 10:
    c += 1
    dice = random.randint(1, 6)
    x = f"[{dice}]"

    if dice == 6:
        x = f"*{x}*"
        count += 1

    command = input("Do you want to play again? (Y/N): ")

if count >= 2:
    print("YOU WON!")

else:
    print("YOU LOSE!")