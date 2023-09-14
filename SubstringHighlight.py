sen = input("Type a sentence: ")
sub = input("Type substring: ")
x = sen.replace(sub, f"*{sub.upper()}*")
print(f"Modified sentence: {x}")