from utilities1 import nameDict

dict2 = {}
keys = []
for i, v in nameDict.items():
    dict2[v] = [i] if v not in dict2.keys() else dict2[v] + [i]

for i in dict2.keys():
    keys.append(i)

for i in keys:
    print(f"Age {i}")

    for j in dict2[i]:
        print(j)