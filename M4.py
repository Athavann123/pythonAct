def countCases(s):
    uc = 0
    lc = 0

    for i in s:
        if i.isupper():
            uc += 1

        if i.islower():
            lc += 1

    print(f"This string has {uc} uppercase characters.")
    print(f"This string has {lc} lowercase characters.")


def flipCase(st):
    return st.swapcase()


def cutQuotedText(st):
    d = st[::-1]
    b = st.split()
    c = 0
    e = 0
    for i in st:
        c = st.find("\"")

    for i in d:
        e = d.find("\"")

    if c == -1 or e == -1:
        return "'ERROR! No quoted text.'"

    else:
        return f'Quote removed: \'{st.replace(st[c:-e], "")}\''


s = input("Enter string with one word with \"quotes\": ")
countCases(s)
print(flipCase(s))
print(cutQuotedText(s))