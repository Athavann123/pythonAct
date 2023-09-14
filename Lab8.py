# Lab 8
# Author: Athavann Thulasiranjan
# Email: athava08@my.yorku.ca
# Student ID: 218658419
# Section B

import random
import time


class snail():
    ani = ["__~@", "_~_@", "~__@"]

    def __init__(self, name):
        assert len(name) == 2, "Initials must be 2 characters."
        self.name = name.upper()
        self.speed = (random.randint(1, 10))/10
        self.frame = 0
        self.pos = 0

    def move(self):
        self.pos = self.pos + self.speed
        self.frame = (self.frame + 1) % 3

        if self.frame > 2:
            self.frame = 0

    def getIntPos(self):
        return int(self.pos)

    def getName(self):
        return self.name

    def getStr(self):
        animation = (" "*self.getIntPos())
        animation = animation+snail.ani[self.frame]
        animation = animation + (" "*(40-self.getIntPos()))
        animation = animation + self.getName()
        return animation


def getSnailList():
    num = int(input("How many snails do you want to race: "))
    n = []
    count = 0
    while count < num:
        count += 1
        name = input("Add initials: ")
        n.append(snail(name))

    return n


def runRace(name):
    com = input("Press enter to start the race: ")
    timestep = 0
    while 1 != 0:
        timestep += 1
        print(40 * "-" + f"Time {timestep}")
        for i in name:
            print(i.getStr())
            i.move()

            x = i.getIntPos()

            if x > 39:
                print(f"{i.getName()} WON!")
                return

        time.sleep(0.2)


def main():
    while 1 != 0:
        runRace(getSnailList())
        com = input("Play again(Y)? ")

        if com.upper() == "Y":
            pass

        else:
            break


if __name__ == "__main__":
    main()