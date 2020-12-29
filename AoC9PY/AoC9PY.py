def findKey(myList):
    start = 0
    end = 25
    curr = 25
    while curr < len(myList):
        success = 0
        for i in range(start, end, 1):
            for j in range(start, end, 1):
                if int(myList[i]) + int(myList[j]) == int(myList[curr]):
                    start += 1
                    end +=1
                    curr +=1
                    success = 1
                    break
            if success == 1:
                break
        if success == 0:
            return myList[curr]
    return 0

def findWeakness(myList, key):
    start = 0
    startOfEx = 0
    endOfEx = 0
    while start < len(myList):
        number = 0
        for i in range(start, len(myList), 1):
            number += int(myList[i])
            if int(number) == int(key):
                startOfEx = start
                endOfEx = i
                break
            if number > int(key):
                break
        if endOfEx != 0:
            break
        start += 1
    min = myList[startOfEx]
    max = int(myList[startOfEx])
    for i in range(startOfEx, endOfEx+1, 1):
        if int(myList[i]) < int(min): min = int(myList[i])
        if int(myList[i]) > int(max): max = int(myList[i])
    result = int(min) + int(max)
    return result

f = open("D:\Documents\AoCinputs\inputday9a.txt")
lista = list(map(lambda x: x.rstrip(), f.readlines()))
key = findKey(lista)
print(key)
print(findWeakness(lista, key))