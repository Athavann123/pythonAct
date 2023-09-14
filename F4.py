import random, time


class SeaLife:
    category = ["fish1", "fish2", "jelly", "crab"]
    draw = {"fish1": ["><>", "<><"], "fish2": [">()", "()<"], "jelly": ["~>)", "(<~"], "crab": ["^_^", "^_^"]}
    speed_range = {"fish1": (5, 10), "fish2": (1, 10), "jelly": (1, 5), "crab": (10, 20)}

    def __init__(self, direction, pos):
        assert direction == 1 or direction == 0, "direction must be 0 or 1"
        assert 0 < pos < 39, "direction must be between 1 and 38"
        self.direction = direction
        self.pos = pos
        self.cat = SeaLife.category[random.randint(0, 3)]
        self.speed = 0

        if self.cat == "fish1":
            self.speed = random.randint(5, 10) / 10

        if self.cat == "fish2":
            self.speed = random.randint(1, 10) / 10

        if self.cat == "jelly":
            self.speed = random.randint(1, 5) / 10

        if self.cat == "crab":
            self.speed = random.randint(10, 20) / 10

    def move(self):
        if self.direction == 0:
            self.pos = self.pos + self.speed

        if self.direction == 1:
            self.pos = self.pos - self.speed

        if self.pos > 40:
            self.direction = 1

        if self.pos < 1:
            self.direction = 0

    def getStr(self):
        animation = (" " * int(self.pos))
        animation = animation + SeaLife.draw[self.cat][random.randint(0, 1)]
        animation = animation + (" " * (40 - int(self.pos)))
        animation = animation + self.cat
        return animation


com = input("Press enter to start aquarium...")
timestep = 0
s1 = SeaLife(random.randint(0, 1), random.randint(5, 30))
s2 = SeaLife(random.randint(0, 1), random.randint(5, 30))
s3 = SeaLife(random.randint(0, 1), random.randint(5, 30))
s4 = SeaLife(random.randint(0, 1), random.randint(5, 30))
s5 = SeaLife(random.randint(0, 1), random.randint(5, 30))
while 1 != 0:
    timestep += 1
    print(40 * "-" + f"Time: {timestep}")
    print(s1.getStr())
    s1.move()
    print(s2.getStr())
    s2.move()
    print(s3.getStr())
    s3.move()
    print(s4.getStr())
    s4.move()
    print(s5.getStr())
    s5.move()
    time.sleep(0.3)

    if timestep == 50:
        break
