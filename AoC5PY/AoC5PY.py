from collections import Counter
def calculateHighestID(myList):
    max = 0
    for i in myList:
        row = 0
        seat = 0
        for j in range(7):
            if i[j] == "B":
                row += pow(2, 6 - int(j))
        for j in range(7, 10):
            if i[j] == "R":
                seat += pow(2, 2-(int(j)-7))
        value = (row * 8) + seat
        if max < value : max= value
    return max

def calculateSeat(myList):
    listRS = []
    listR = []
    listS = []
    R = 0
    S = 0
    for i in myList:
        row = 0
        seat = 0
        for j in range(7):
            if i[j] == "B":
                row += pow(2, 6 - int(j))
        for j in range(7, 10):
            if i[j] == "R":
                seat += pow(2, 2-(int(j)-7))
        value = [row, seat]
        listR.append(row)
        listRS.append(value)
    x=Counter(listR)
    for i in range(128):
        if x[i] == 7:
            R = i
            for j in listRS:
                if i in j:
                    listS.append(j[1])
    for i in range(8):
        if i not in listS: S = i
    return R*8+S

f = open("D:\Documents\AoCinputs\inputday5a.txt")
lista = list(map(lambda x: x.rstrip(), f.readlines()))
print(calculateHighestID(lista))
print(calculateSeat(lista))