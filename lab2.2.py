sen = input("Type a long string: ")
final_sen = sen.upper()
l = final_sen.replace("T", "+").replace("A", "@").replace("E", "3").\
    replace("I", "|").replace("B", "8").replace("O", "0").\
    replace("C", "[").replace("S", "5")

print(l)