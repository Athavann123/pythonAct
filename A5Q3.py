import random
count = 0

while 1 != 0:
    count += 1
    answer = random.randint(1,10)
    print(f"Round {count}:")
    print("Guess a number from 1 to 10. Enter -1 to exit.")
    guess = int(input("Your guess: "))

    if guess == -1:
        break

    if guess != answer:
        print(f"Sorry but the number I have is {answer}")

    if guess == answer:
        print(f"Correct. My number is {answer}")

    print("\n")