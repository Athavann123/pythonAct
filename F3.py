from utilities import students
from utilities import studentsInfo


def check(alist, index):
    for i in alist:
        if i == index:
            return True

    return False

finaldict = {}


for i in range(len(students)):
    year = ""

    if check(studentsInfo['Year 1'], i):
        year = "Year 1"

    elif check(studentsInfo['Year 2'], i):
        year = "Year 2"

    elif check(studentsInfo['Year 3'], i):
        year = "Year 3"

    elif check(studentsInfo['Year 4'], i):
        year = "Year 4"

    program = ""

    if check(studentsInfo['CS'], i):
        program = "CS"

    elif check(studentsInfo['DM'], i):
        program = "DM"

    elif check(studentsInfo['BZ'], i):
        program = "BZ"

    elif check(studentsInfo['SE'], i):
        program = "SE"

    housing = ""

    if check(studentsInfo['On Campus'], i):
        housing = "On Campus"

    if check(studentsInfo['Off Campus'], i):
        housing = "Off Campus"

    finaldict[students[i]] = "{0:>10} ({1}) Program: {2} Housing: {3}".format(students[i], year, program, housing)


for i in sorted(finaldict):
    print(finaldict[i])