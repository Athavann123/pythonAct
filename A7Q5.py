import random
ex = ""
card_value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
card_suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
card_deck = []
for i in range(52):
    card_deck.append(card_value[i % 13] + " of " + card_suits[i // 13])

while 1 != 0:
    ex = input("Press enter to shuffle deck, type 'exit' to quit: ")

    if ex == "exit":
        break

    else:
        random.shuffle(card_deck)

        for i in card_deck:
            print(i)