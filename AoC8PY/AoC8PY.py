def runCode(myList):
    numberOfOcc = list()
    accumulator = 0
    for i in range(len(myList)):
        numberOfOcc.append(int(0))
    i = 0
    while i < len(myList):
        func = myList[i].split(" ")[0]
        num = myList[i].split(" ")[1]
        if "acc" in func:
            if numberOfOcc[i] == 1:
                return accumulator
            numberOfOcc[i] = 1
            accumulator += int(num)
            i += 1
            continue
        if "jmp" in func:
            if numberOfOcc[i] == 1:
                return accumulator
            numberOfOcc[i] = 1
            i += int(num)
            continue
        if "nop" in func:
            if numberOfOcc[i] == 1:
                return accumulator
            numberOfOcc[i] = 1
            i += 1
            continue

def fixCode(myList):
    i = 0
    helpList = myList.copy()
    for k in range(len(myList)):
        numberOfOcc = list()
        accumulator = 0
        for i in range(len(myList)):
            numberOfOcc.append(int(0))
        myList = helpList.copy()
        if "acc" in myList[k]:
            continue
        x = 0
        if "nop" in myList[k]:
            myList[k] = myList[k].replace("nop", "jmp")
            x = 1
        if x == 0:
            myList[k] = myList[k].replace("jmp", "nop")
        i = 0
        while i < len(myList) + 1:
            if i == len(myList):
                return "fixed", accumulator
            func = myList[i].split(" ")[0]
            num = myList[i].split(" ")[1]
            if "acc" in func:
                if numberOfOcc[i] == 1:
                    break
                numberOfOcc[i] = 1
                accumulator += int(num)
                i += 1
                continue
            if "jmp" in func:
                if numberOfOcc[i] == 1:
                    break
                numberOfOcc[i] = 1
                i += int(num)
                continue
            if "nop" in func:
                if numberOfOcc[i] == 1:
                    break
                numberOfOcc[i] = 1
                i += 1
                continue    


f = open("D:\Documents\AoCinputs\inputday8a.txt")
lista = list(map(lambda x: x.rstrip(), f.readlines()))
print(runCode(lista))
print(fixCode(lista))
