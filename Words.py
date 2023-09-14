number = int(input("How many words do you want to enter: "))
stored_words = ""

if number <= 0:
    print("Invalid answer")

else:
    for i in range(number):
        words = input("Type a word: ")
        stored_words = stored_words + " " + words

print(stored_words)
