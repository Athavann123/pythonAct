def insertItem(blist, item, printResult=False / True):
    count = -1
    if len(blist) == 0:
        blist.append(item)

    elif item >= blist[-1]:
        blist.append(item)

    else:
        while count < len(blist)-1:
            count += 1
            if item < blist[count]:
                break

        blist.insert(count, item)

    print(blist)


alist = [10, 11, 99, 1, 34, 88]
alist.sort()
insertItem(alist, 15)