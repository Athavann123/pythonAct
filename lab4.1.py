import random


def getCardValue():
    return random.randint(2, 14)


def getCardStr(cardvalue):
    if cardvalue == 10:
        return "T"

    elif cardvalue == 11:
        return "J"

    elif cardvalue == 12:
        return "Q"

    elif cardvalue == 13:
        return "K"

    elif cardvalue == 14:
        return "A"

    else:
        return str(cardvalue)


def getHLGuess():
    x = ""
    while 1 != 0:
        guess = input("High or Low (H/L)?: ")

        if guess == "h" or guess == "H":
            x = "HIGH"
            break

        if guess == "l" or guess == "L":
            x = "LOW"
            break

        else:
            pass

    return x


def getBetAmount(maximum):
    while 1 != 0:
        bet = int(input("Input bet amount: "))
        if bet >= 1 and bet <= maximum:
            break

        else:
            pass

    return bet


def playerGuessCorrect(card1, card2, betType):
    if card2 > card1 and betType == "HIGH":
        return True

    elif card2 > card1 and betType == "LOW":
        return False

    elif card2 < card1 and betType == "HIGH":
        return False

    elif card2 < card1 and betType == "LOW":
        return True

    elif card2 == card1:
        return False


count = 0
points = 100
while count < 10:
    card1 = getCardValue()
    card2 = getCardValue()
    count += 1
    print("-------------------------------------")
    print(f"OVERALL POINTS: {points} ROUND {count}/10")
    print(f"First card is a [{getCardStr(card1)}]")
    x = getHLGuess()
    y = getBetAmount(points)
    print(f"Second card is a [{getCardStr(card2)}]")

    if playerGuessCorrect(card1, card2, x):
        print(f"Card1 [{getCardStr(card1)}] Card2 [{getCardStr(card2)}] - You bet '{x}' for {y} - YOU WON")
        points += y

    else:
        print(f"Card1 [{getCardStr(card1)}] Card2 [{getCardStr(card2)}] - You bet '{x}' for {y} - YOU LOST")
        points -= y

    if points >= 500:
        print("---------------WIN--------------------")
        print(f"YOU MADE IT TO *{points}* POINTS IN {count} ROUNDS!")
        print("--------------------------------------")
        break

    if points <= 0:
        print("---------------LOSE--------------------")
        print(f"YOU HAVE *{points}* POINTS AFTER {count} ROUNDS!")
        print("--------------------------------------")
        break

    if count == 10:
        print("-----------LOSE-------------")
        print(f"ONLY *{points}* POINTS IN 10 ROUNDS!")
        print("-----------------------------")

