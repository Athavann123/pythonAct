try:
    age = int(input("Age: "))
    income = 20000
    risk = income/age
    print(risk)
    print(age)

except ValueError:
    print("Not a number")

except ZeroDivisionError:
    print("Zero is not an age number")