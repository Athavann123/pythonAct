name = input("Name: ")
weight = float(input("Weight (kg): "))
height = float(input("Height (cm): "))
meter = height / 100
bmi = weight / (meter ** 2)

print(f"Name: {name.title()} Weight: %.2f Height [meters]: %.2f BMI: %.2f" %(weight, meter, bmi))