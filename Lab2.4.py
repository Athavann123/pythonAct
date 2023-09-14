a = input("Input numbers to multiply: ")
ex_numbers = a.split()
print(f"Extracted numbers: {ex_numbers[0]}, {ex_numbers[2]}")
print(f"{int(ex_numbers[0])} * {int(ex_numbers[2])} = {int(ex_numbers[0]) * int(ex_numbers[2])}")
