#######################
# Lab 6 - Starting code
# Name: Athavann Thulasiranjan
# Student ID: 218658419
# email: athava08@my.yorku.ca
# Section: B
#######################

# variables for task 1
dictMenu = {'Fruits': {'Apple': 1.99, 'Banana': 0.59, 'Kiwi': 1.1, 'Grapes': 2.99, 'Pear': 2.15},
            'Drinks': {'Water': 1.0, 'Juice': 3.5, 'Coffee': 1.5, 'Soda': 1.5, 'Tea': 1.25},
            'Dessert': {'Ice Cream': 2.99, 'Pie': 2.5, 'Cake': 2.75},
            'Main Dishes': {'Masala Dosa': 4.25, 'Jianbing': 2.88, 'Falafel': 5.15, 'Pizza': 8.5}}

# variables for task 2
decoder = {80: 'P', 121: 'y', 116: 't', 104: 'h', 111: 'o', 110: 'n', 105: 'i', 115: 's', 99: 'c', 108: 'l', 46: '.',
           32: ' ', 44: ',', 45: '-', 95: '_', 40: '(', 42: '*', 41: ')', 47: '/', 92: '\\', 61: '=', 39: "'", 124: '|',
           96: '`', 58: ':', 59: ';'}
msg1 = [[80, 121, 116, 104, 111, 110], [105, 115], [99, 111, 111, 108, 46]]
msg2 = [[32, 32, 32, 44, 45, 46], [32, 95, 40, 42, 95, 42, 41, 95], [40, 95, 32, 32, 111, 32, 32, 95, 41],
        [32, 32, 47, 32, 111, 32, 92], [32, 40, 95, 47, 32, 92, 95, 41, 32]]
msg3 = [[32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 40], [32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 41],
        [32, 32, 32, 32, 32, 95, 95, 46, 46, 45, 45, 45, 46, 46, 95, 95],
        [32, 44, 45, 61, 39, 32, 32, 47, 32, 32, 124, 32, 32, 92, 32, 32, 96, 61, 45, 46],
        [58, 45, 45, 46, 46, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 46, 46, 45, 45, 59],
        [32, 92, 46, 44, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 44, 46, 47]]


def task1():
    def menu(d):
        print("----Fruits----")
        for i in dictMenu['Fruits']:
            print(f"${dictMenu['Fruits'][f'{i}']:.2f} {i}")

        print("----Drinks----")
        for j in dictMenu['Drinks']:
            print(f"${dictMenu['Drinks'][f'{j}']:.2f} {j}")

        print("----Dessert----")
        for k in dictMenu['Dessert']:
            print(f"${dictMenu['Dessert'][f'{k}']:.2f} {k}")

        print("----Main Dishes----")
        for l in dictMenu['Main Dishes']:
            print(f"${dictMenu['Main Dishes'][f'{l}']:.2f} {l}")

    menu(dictMenu)


def task2():
    def m1(d, m):
        s1 = ""
        s2 = ""
        s3 = ""
        for i in m[0]:
            s1 = s1 + decoder[i]

        for i in m[1]:
            s2 = s2 + decoder[i]

        for i in m[2]:
            s3 = s3 + decoder[i]

        print("--- Message 1 ----")
        print(s1)
        print(s2)
        print(s3)

    def ms2(d, m):
        s1 = ""
        s2 = ""
        s3 = ""
        s4 = ""
        s5 = ""
        s6 = ""

        for i in m[0]:
            s1 = s1 + decoder[i]

        for i in m[1]:
            s2 = s2 + decoder[i]

        for i in m[2]:
            s3 = s3 + decoder[i]

        for i in m[3]:
            s4 = s4 + decoder[i]

        for i in m[4]:
            s5 = s5 + decoder[i]

        print("--- Message 2 ----")
        print(s1)
        print(s2)
        print(s3)
        print(s4)
        print(s5)

    def ms3(d, m):
        s1 = ""
        s2 = ""
        s3 = ""
        s4 = ""
        s5 = ""
        s6 = ""

        for i in m[0]:
            s1 = s1 + decoder[i]

        for i in m[1]:
            s2 = s2 + decoder[i]

        for i in m[2]:
            s3 = s3 + decoder[i]

        for i in m[3]:
            s4 = s4 + decoder[i]

        for i in m[4]:
            s5 = s5 + decoder[i]

        for i in m[5]:
            s6 = s6 + decoder[i]

        print("--- Message 3 ----")
        print(s1)
        print(s2)
        print(s3)
        print(s4)
        print(s5)
        print(s6)

    m1(decoder, msg1)
    ms2(decoder, msg2)
    ms3(decoder, msg3)


def main():
    print("------ Task 1 ------")
    task1()

    print("------ Task 2 ------")
    task2()

    input('Press enter to finish.')


if __name__ == '__main__':
    main()
