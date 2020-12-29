lookingFor = set()
lookingFor.add("shiny gold bag")
fullSet = set()

def recursiveBagSearcher(myList, LFSet):
    newLFSet = set()
    for i in myList:
        for j in LFSet:
            if j in i.split("s contain")[1]:
                newLFSet.add(i.split("s contain")[0])
    helpSet = newLFSet.difference(fullSet)
    if len(helpSet) == 0:
        return
    fullSet.update(helpSet)
    recursiveBagSearcher(myList, helpSet)
    return

def calculateNoOfBags(myList, bag):
    counter = 0
    for i in myList:
        if bag in i.split("s contain")[0]:
            bagsLine = i.split("s contain ")[1]
            bagsLine = bagsLine.replace('.','')
            bagsList = bagsLine.split(", ")
            if "no other bag" in bagsLine:
                return 1
            for j in bagsList:
                number = int(j.split(" ", 1)[0])
                newBag = j.split(" ", 1)[1]
                newBag = newBag.replace("bags", "bag")
                print(newBag)
                nob = int(calculateNoOfBags(myList, newBag))
                if nob == 1 and number == 1:
                    counter += number+nob
                    continue
                counter += number*nob
            return counter
    return 1


f = open("D:\Documents\AoCinputs\inputday7a.txt")
lista = list(map(lambda x: x.rstrip(), f.readlines()))
recursiveBagSearcher(lista, lookingFor)
print(len(fullSet))
print(calculateNoOfBags(lista, "shiny gold bag"))
