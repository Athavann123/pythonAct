import RPS

player1 = input("What is your name: ")
player2 = "CPU"
play = input("Are you ready to play(Y/N): ")
if play == "Y":
    RPS.play(player1, player2)

elif play == "N":
    exit()