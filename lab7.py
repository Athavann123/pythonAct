# Lab 7
# Author: Athavann Thulasiranjan
# Email: athava08@my.yorku.ca
# Student ID: 218658419

import pytest
from typing import List

# Accepts a list of integers
def initializeMinMaxList(myList: List[int]) -> None:   # given
    myList.sort()

def insertItem(myList: List[int], item: int) -> None:  # given
    myList.append(item)
    myList.sort()

def getMinMax(myList: List[int], minormax: str) -> int:   # given -- but requires additional assert
    assert minormax.upper()=="MAX" or minormax.upper()=="MIN", "2nd argument must be 'Min' or 'Max' "
    assert len(myList) != 0, "The list is empty"
    result: int
    if minormax == "MAX":
        result = myList[-1]
        del myList[-1]
    else:
        result = myList[0]
        del myList[0]
    return result

# Main function is given.
def main():
    aList = [10, 11, 99, 1, 55, 100, 34, 88]
    print("Starting List: ", aList)
    initializeMinMaxList(aList)
    min1 = getMinMax(aList, "MIN")
    print("1st min: %d" % (min1))
    min2 = getMinMax(aList, "MIN")
    print("2nd min: %d" % (min2))
    max1 = getMinMax(aList, "MAX")
    print("1st max: %d" % (max1))
    max2 = getMinMax(aList, "MAX")
    print("2nd max: %d" % (max2))

    print("Insert %d %d %d %d" % (min1 - 1, min2 - 1, max1 + 1, max2 + 1))
    insertItem(aList, min1 - 1)
    insertItem(aList, min2 - 1)
    insertItem(aList, max1 + 1)
    insertItem(aList, max2 + 1)

    min1 = getMinMax(aList, "MIN")
    print("1st min: %d" % (min1))
    min2 = getMinMax(aList, "MIN")
    print("2nd min: %d" % (min2))
    max1 = getMinMax(aList, "MAX")
    print("1st max: %d" % (max1))
    max2 = getMinMax(aList, "MAX")
    print("2nd max: %d" % (max2))

    #print("DONE.  Type Enter to exit.")
    #input()


if __name__ == "__main__":
    main()


#####
# WRITE YOUR TEST CASES BELOW HERE
#
######

def test_getMinMaxCase1():
    blist = [1, 20]
    initializeMinMaxList(blist)
    min1 = getMinMax(blist, "MIN")
    max1 = getMinMax(blist, "MAX")
    assert min1 == 1, "Min should be 1"
    assert max1 == 20, "Max should be 20"

def test_getMinMaxCase2():
    clist = ["y"]
    initializeMinMaxList(clist)
    min2 = getMinMax(clist, "MIN")
    assert min2, "Min should be y"
    insertItem(clist, min2)
    max2 = getMinMax(clist, "MAX")
    assert max2, "Max should be y"

def test_getMinMaxCase3():
    dlist = []
    initializeMinMaxList(dlist)
    insertItem(dlist, "x")
    insertItem(dlist, "y")
    min3 = getMinMax(dlist, "MIN")
    assert min3, "Min should be x"
    max3 = getMinMax(dlist, "MAX")
    assert max3, "Max should be y"


def test_getMinMaxRequestError():
    elist = [10, 20, 30]
    initializeMinMaxList(elist)
    with pytest.raises(AssertionError):
        assert str(getMinMax(elist, "MID").value) == "AssertionError", "Should raise AssertionError!"

def test_getMinMaxEmptyError():
    flist = []
    initializeMinMaxList(flist)
    with pytest.raises(AssertionError):
        assert str(getMinMax(flist, "MIN").value) == "AssertionError", "Should raise AssertionError!"