import random


def print_deck(card_deck):
    for i in card_deck:
        print(i)


def shuffle_deck(card_deck):
    new_deck = []
    for i in card_deck:
        new_deck.append(i)

    random.shuffle(new_deck)

    for i in new_deck:
        print(i)

def hand_deck(card_deck, hand, num):
    count = 0
    s = 51
    shuffle = []
    random.shuffle(card_deck)

    for i in card_deck:
        shuffle.append(i)

    while count < hand:
        count += 1
        s -= 1
        print(f"Hand # {count}")
        for i in range(num):
            print(shuffle[random.randint(i, s)])

        print("\n")


card_value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
card_suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
card_deck = []

for i in range(52):
    card_deck.append(card_value[i % 13] + " of " + card_suits[i // 13])

while 1 != 0:
    print("Options:")
    print("0: Exit")
    print("1: Print standard deck")
    print("2: Print shuffled deck")
    print("3: Deck based on hand")
    option = int(input("Enter a number based on the options: "))

    if option == 0:
        break

    elif option == 1:
        print_deck(card_deck)

    elif option == 2:
        shuffle_deck(card_deck)

    elif option == 3:
        hand = int(input("How many hand decks do you want? "))
        num = int(input("How many cards per hand? "))
        hand_deck(card_deck, hand, num)

    print("\n")