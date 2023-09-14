def greet_user(name, last_name):
    print(f"Hi {name} {last_name}!")
    print("Welcome aboard")
    pass


name = input("What is your name: ")
last = input("What is your last name: ")

print("Start")
greet_user(name, last)
print("Finish")