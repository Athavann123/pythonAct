class Name:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi I am {self.name}")


name = input("What is your name: ")
nm = Name(name)
nm.talk()