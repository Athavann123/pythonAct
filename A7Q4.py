import random
card_value = []
count = 1
card_count = 0
while count <= 7:
    count += 1
    number = random.randint(1, 13)

    if number == 1:
        card_value.append("Ace")

    if number == 2:
        card_value.append("Two")

    if number == 3:
        card_value.append("Three")

    if number == 4:
        card_value.append("Four")

    if number == 5:
        card_value.append("Five")

    if number == 6:
        card_value.append("Six")

    if number == 7:
        card_value.append("Seven")

    if number == 8:
        card_value.append("Eight")

    if number == 9:
        card_value.append("Nine")

    if number == 10:
        card_value.append("Ten")

    if number == 11:
        card_value.append("Jack")

    if number == 12:
        card_value.append("Queen")

    if number == 13:
        card_value.append("King")

for i in card_value:
    print(i)

print("\n")
search = input("Type a card value to search: ")

for i in card_value:
    if search == i:
        card_count += 1

print(f"There are {card_count} {search} in your hand")