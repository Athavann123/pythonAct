import random


def play(player1, player2):
    while 1 != 0:
        print("Player 1 and Player 2 each get the following options: ")
        print("0: Quit")
        print("1: Rock")
        print("2: Paper")
        print("3: Scissors")
        p1 = int(input(f"{player1} rock, paper, or scissors: "))
        p2 = random.randint(1, 3)

        print(f"{player1} chose {p1}")
        print(f"{player2} chose {p2}")

        if p1 == 0:
            break

        elif p1 == 1 and p2 == 3:
            print(f"{player1} wins")

        elif p1 == 2 and p2 == 1:
            print(f"{player1} wins")

        elif p1 == 3 and p2 == 2:
            print(f"{player1} wins")

        elif p1 == 1 and p2 == 2:
            print(f"{player2} wins")

        elif p1 == 2 and p2 == 3:
            print(f"{player2} wins")

        elif p1 == 3 and p2 == 1:
            print(f"{player2} wins")

        else:
            print("It is a tie")

        print("\n")