numbers = {
    0: "Zero",
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine"
}

phone = int(input("Phone: "))
stored_num = ""

for i in str(phone):
    if "1" in i:
        stored_num = stored_num + " " + numbers[1]

    if "2" in i:
        stored_num = stored_num + " " + numbers[2]

    if "3" in i:
        stored_num = stored_num + " " + numbers[3]

    if "4" in i:
        stored_num = stored_num + " " + numbers[4]

    if "5" in i:
        stored_num = stored_num + " " + numbers[5]

    if "6" in i:
        stored_num = stored_num + " " + numbers[6]

    if "7" in i:
        stored_num = stored_num + " " + numbers[7]

    if "8" in i:
        stored_num = stored_num + " " + numbers[8]

    if "9" in i:
        stored_num = stored_num + " " + numbers[9]

    if "0" in i:
        stored_num = stored_num + " " + numbers[0]

print(stored_num)