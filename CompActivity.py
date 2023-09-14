username = input("Enter username: ")

if len(username) < 3:
    print("Name must be at least 3 characters")

elif len(username) > 50:
    print("Name must be a maximum of 50 characters")

else:
    print("Name looks good!")