class Student:
    def __init__(self):
        self.name = ""
        self.mark1 = 0
        self.mark2 = 0
        self.mark3 = 0

    def add_student(self, name):
        self.name = name

    def get_student(self):
        return self.name

    def add_mark(self, option, mark):
        if option == 1:
            self.mark1 = mark

        if option == 2:
            self.mark2 = mark

        if option == 3:
            self.mark3 = mark

    def get_mark(self, option):
        if option == 1:
            print(self.mark1)

        if option == 2:
            print(self.mark2)

        if option == 3:
            print(self.mark3)

    def get_average(self):
        average = (self.mark1 + self.mark2 + self.mark3)/3
        print(f"Your average is {average}")

    def get_highmark(self):
        print(max(self.mark1, self.mark2, self.mark3))

    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Test Mark 1: {self.mark1}")
        print(f"Test Mark 2: {self.mark2}")
        print(f"Test Mark 3: {self.mark3}")