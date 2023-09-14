word = "Athavann"
new_word = word.lower()
hang_answer = []
answer = []
guess = []
for i in list(new_word):
    answer.append(i)

for i in answer:
    if answer.count(i) > 1:
        answer.remove(i)

count = 6

while count > 0:
    hang_guess = input("Enter a lower case character or the entire word to win: ")

    if len(hang_guess) > 1 and hang_guess != new_word:
        print("Wrong answer.")
        print(f"{count} lives remaining")
        count -= 1

    if hang_guess == new_word:
        print("You win")
        print(f"The answer was {word}")
        break

    if len(hang_guess) == 1:
        for i in answer:
            if hang_guess.count(i) == 1:
                print(f"A/An {hang_guess} has been found {new_word.count(hang_guess)} times")
                hang_answer.append(hang_guess)
                break

    if len(hang_answer) == len(answer):
        hang_answer.sort()
        guess.sort()

        for i in range(len(hang_answer)):
            if hang_answer[i] == answer[i]:
                print("You win")
                exit()

    if count == 0:
        print("You lose")