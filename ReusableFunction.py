def emoji_converter(message):
    emoji = {
        ":)": "😀",
        ":(": "😔"
    }

    if ":)" in message:
        return (message.replace(":)", emoji[":)"]))

    elif ":(" in message:
        return message.replace(":(", emoji[":("])


message = input(">")
print(emoji_converter(message))