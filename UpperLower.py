sen = input("Type a sentence: ")
s = sen.lower()
print(f"The string is {len(s)} chars long. {s[len(s)//2]} is the middle character.")
print(s[0:len(s)//2].upper() + "|" + s[len(s)//2:])
