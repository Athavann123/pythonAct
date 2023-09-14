temp = float(input("Input temperature: "))
unit = input("Is it Celsius or Fahrenheit (C or F): ")
C_to_F = (temp * 9/5) + 32
F_to_C = (temp - 32) * (5/9)

if unit == "C":
    print(f"The temperature is {C_to_F}°F")

elif unit == "F":
    print(f"The temperature is {F_to_C}°C")

else:
    print("Invalid")