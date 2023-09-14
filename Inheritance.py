class Mammal:
    def walk(self):
        print("Walk")


class Dog(Mammal):
    def bark(self):
        print("Bark")


class Cat(Mammal):
    def be_annoying(self):
        print("annoying")


dog1 = Dog()
cat1 = Cat()
dog1.walk()
dog1.bark()
cat1.be_annoying()
