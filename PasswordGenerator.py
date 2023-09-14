import random
import string

letters = list(string.ascii_letters)
char = [".", "!", "@", "#", "$", "%", "^", "/", "*", "(", ")", "&", ">", ":", "{", "}", "[", "]", ";"]
all_characters = []

for i in letters:
    all_characters.append(i)

for i in char:
    all_characters.append(i)

while 1 != 0:
    password = ""
    random.shuffle(all_characters)
    num = int(input("How many characters do you want for password (must be longer than 8: ): "))

    if num <= 8:
        print("Password is less than required characters.")

    else:
        for i in range(num):
            password = password + all_characters[i]

    print(f"Generated password {password}")
    print("\n")