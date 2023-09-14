decoder = {80: 'P', 121: 'y', 116: 't', 104: 'h', 111: 'o', 110: 'n', 105: 'i', 115: 's', 99: 'c', 108: 'l', 46: '.', 32: ' ', 44: ',', 45: '-', 95: '_', 40: '(', 42: '*', 41: ')', 47: '/', 92: '\\', 61: '=', 39: "'", 124: '|', 96: '`', 58: ':', 59: ';'}
msg1 = [[80, 121, 116, 104, 111, 110], [105, 115], [99, 111, 111, 108, 46]]
msg2 = [[32, 32, 32, 44, 45, 46], [32, 95, 40, 42, 95, 42, 41, 95], [40, 95, 32, 32, 111, 32, 32, 95, 41], [32, 32, 47, 32, 111, 32, 92], [32, 40, 95, 47, 32, 92, 95, 41, 32]]
msg3 = [[32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 40], [32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 41], [32, 32, 32, 32, 32, 95, 95, 46, 46, 45, 45, 45, 46, 46, 95, 95], [32, 44, 45, 61, 39, 32, 32, 47, 32, 32, 124, 32, 32, 92, 32, 32, 96, 61, 45, 46], [58, 45, 45, 46, 46, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 46, 46, 45, 45, 59], [32, 92, 46, 44, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 44, 46, 47]]
ms1 = ""
s = ""


def ms(d, m):
    s1 = ""
    s2 = ""
    s3 = ""
    for i in m[0]:
        s1 = s1 + decoder[i]

    for i in m[1]:
        s2 = s2 + decoder[i]

    for i in m[2]:
        s3 = s3 + decoder[i]

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

    print(s1)
    print(s2)
    print(s3)
    print(s4)
    print(s5)
    print(s6)


ms(decoder, msg1)
ms2(decoder, msg2)
ms3(decoder, msg3)