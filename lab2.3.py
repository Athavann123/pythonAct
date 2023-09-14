sen = input("Input a long string: ")
final_sen = sen.upper()

print(f"This string is {len(sen)} characters long. The middle character is '{final_sen[len(sen) // 2]}' ")
print("Flipped String")
print(f"{final_sen[len(final_sen) // 2:]} |{final_sen[0:len(final_sen) // 2]}")