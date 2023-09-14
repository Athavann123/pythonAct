number = 9
count = 1

while count <= 3:
    count += 1
    guess = int(input("Guess: "))

    if guess == number:
        print("You have guessed the number")
        break

    if count > 3:
        print("You failed")
