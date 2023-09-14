import random

print("Rock, Paper, Scissors!")
while 1 != 0:
    print("Make your selection. . .")
    rps = {1: "rock", 2: "paper", 3: "scissors"}
    p1 = int(input("(1) rock, (2) paper, (3) scissors? "))
    p2 = random.randint(1, 3)

    if p1 < 1 or p1 > 3:
        print("Invalid selection. Try again.")

    else:
        print(f"You: {rps[p1]}")
        print(f"HAL: {rps[p2]}")
        if p1 == 1 and p2 == 3:
            print(f"You win")

        elif p1 == 2 and p2 == 1:
            print(f"You win")

        elif p1 == 3 and p2 == 2:
            print(f"You win")

        elif p1 == 1 and p2 == 2:
            print(f"HAL wins")

        elif p1 == 2 and p2 == 3:
            print(f"HAL wins")

        elif p1 == 3 and p2 == 1:
            print(f"HAL wins")

        else:
            print("A tie")

        cmd = input("Play again (Y/N)? ")

        if cmd.upper() == "N":
            break

        else:
            pass

        print("\n")
