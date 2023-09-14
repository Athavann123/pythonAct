emoji = {
    ":)": "😀",
    ":(": "😔"
}

command = input(">")

if ":)" in command:
    print(command.replace(":)", emoji[":)"]))

elif ":(" in command:
    print(command.replace(":(", emoji[":("]))