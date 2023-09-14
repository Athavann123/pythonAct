import converters

weight = int(input("What is your weight: "))
unit = input("Is your weight lbs or kg? ")

if unit == "lbs":
    print(f"Your weight is {converters.lbs_to_kg(weight)} kg")

elif unit == "kg":
    print(f"Your weight is {converters.kg_to_lbs(weight)} lbs")