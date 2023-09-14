from random import randint

# variable for task 1
lyrics = """It might seem crazy what I'm 'bout to say
Sunshine she's here, you can take a break
I'm a hot air balloon that could go to space
With the air, like I don't care baby by the way
Huh, because I'm happy
Clap along if you feel like a room without a roof
Because I'm happy
Clap along if you feel like happiness is the truth
Because I'm happy
Clap along if you know what happiness is to you
Because I'm happy
Clap along if you feel like that's what you wanna do."""

# variable for task2
nameDict = {"Kai":19, "Bailey":19, "Su":21, "Mahesh":18, "Abdullah":18,
            "Dirk":17, "Franck":18, "Ollie":19, "Parsa":19, "Svetlana":24, "Jol":20, "Abbo":21,
            "Xavier":18, "Sarah":17, "Ming":19, "Seonjoo":20, "Pravel":22, "Urzula":22, "Javier":19,
            "Beatrice":20, "Olivia":21, "Bosko":17, "Katja":23, "Maxim":18, "Cameron":17, "Priya":18}

# variable for task3
raster = [['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
          ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']]

# variable for task 4
numList = [21, 20, 29, 16, 16, 19, 26, 19, 26, 23, 19, 25, 16, 18, 18, 18, 21, 15, 18,
           14, 22, 17, 32, 30, 22, 28, 26, 17, 19, 16, 17, 17, 19, 21, 20, 17, 18, 34, 23,
           18, 23, 22, 17, 22, 16, 11, 21, 26, 20, 27]


class listStats():

    def __init__(self, numList, corruption_level):
        self.list = numList[:]
        self.corruption_level = corruption_level

        for i in range(len(self.list)):

            if randint(0, 100) <= corruption_level:
                r = randint(0, 100)

                if r > 50:
                    self.list[i] = -1

                else:
                    self.list[i] = 100

    def computeMean(self):
        sum = 0

        for i in self.list:
            sum = sum + i

        avg = sum/len(self.list)

        print(f"Standard Mean {avg:.2f}")

    def computeTrimmedMean(self):
        tlist = self.list[10:-10]
        tlist.sort()
        s = 0

        for i in tlist:
            s = s + i

        print(f"Trimmed Mean {s/len(tlist):.2f}")

    def computeMedian(self):
        self.list.sort()

        print(f"Median {self.list[len(self.list) // 2]}")

    def printStatistics(self):
        print(f"Corruption Level {self.corruption_level}%")
        print(self.list)
        self.computeMean()
        self.computeTrimmedMean()
        self.computeMedian()
