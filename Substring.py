sentence = input("Type a sentence: ")
substring = input("Enter substring: ")

if sentence.count(substring):
    print(sentence.replace(substring, f"*{substring.upper()}*"))