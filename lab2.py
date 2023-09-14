################
# Lab 2
# Author: Athavann Thulasiranjan
# Email: athava08@my.yorku.ca
# Student ID: 218658419
# Section B

print("\n----Task 1---- BMI Calculator")
name = input("Name: ")
weight = float(input("Weight (kg): "))
height = float(input("Height (cm): "))
meter = height / 100
bmi = weight / (meter ** 2)

print(f"Name: {name.title()} Weight: %.2f Height [meters]: %.2f BMI: %.2f" %(weight, meter, bmi))

print("\n----Task 2---- Leetspeak Converter")
sen = input("Type a long string: ")
final_sen = sen.upper()
l = final_sen.replace("T", "+").replace("A", "@").replace("E", "3").\
    replace("I", "|").replace("B", "8").replace("O", "0").\
    replace("C", "[").replace("S", "5")

print(l)

print("\n----Task 3---- Flipping String")
sen = input("Input a long string: ")
final_sen = sen.upper()

print(f"This string is {len(sen)} characters long. The middle character is '{final_sen[len(sen) // 2]}' ")
print("Flipped String")
print(f"{final_sen[len(final_sen) // 2:]} |{final_sen[0:len(final_sen) // 2]}")

print("\n----Task 4---- Multiple numbers")
a = input("Input numbers to multiply: ")
ex_numbers = a.split()
print(f"Extracted numbers: {ex_numbers[0]}, {ex_numbers[2]}")
print(f"{int(ex_numbers[0])} * {int(ex_numbers[2])} = {int(ex_numbers[0]) * int(ex_numbers[2])}")


input("Press enter to exit. ")  # input statement to pause code when finished