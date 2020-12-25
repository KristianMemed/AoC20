from collections import Counter

def calcSolutiona(myList):
    count = 0
    chckSet = set()
    for i in myList:
        if not i:
            count += len(chckSet)
            chckSet.clear()
            continue   
        for j in i:
            chckSet.add(j)
    count += len(chckSet)
    return count

def calcSolutionb(myList):
    count = 0
    countOfPeople = 0
    chckSet = set()
    chckList = []
    for i in myList:
        if not i:
            helpCounter = Counter(chckList)
            for k in chckSet:
                if helpCounter[k] == countOfPeople:
                    count += 1
            chckList.clear()
            chckSet.clear()
            countOfPeople = 0
            continue
        for j in i:
            chckSet.add(j)
            chckList.append(j)
        countOfPeople += 1
    helpCounter = Counter(chckList)
    for k in chckSet:
        if helpCounter[k] == countOfPeople:
            count += 1
    return count

f = open("D:\Documents\AoCinputs\inputday6a.txt")
lista = list(map(lambda x: x.rstrip(), f.readlines()))
print(calcSolutiona(lista))
print(calcSolutionb(lista))