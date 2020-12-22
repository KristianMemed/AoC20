def counterA(myList):
    counter = 0
    for i in myList:
        line = i.split(": ")
        rule = line[0]
        password = line[1]
        rulekey = rule.split(" ")[1]
        number = rule.split(" ")[0]
        min = int(number.split("-")[0])
        max = int(number.split("-")[1])
        keycount = password.count(rulekey)
        if min <= keycount and keycount <= max:
            counter += 1
    return counter

def counterB(myList):
    counter = 0
    for i in myList:
        occurenceCount = 0
        line = i.split(": ")
        rule = line[0]
        password = line[1]
        rulekey = rule.split(" ")[1]
        number = rule.split(" ")[0]
        first = int(number.split("-")[0]) - 1
        second = int(number.split("-")[1]) - 1
        if password[first] == rulekey: occurenceCount += 1
        if password[second] == rulekey: occurenceCount += 1
        if occurenceCount == 1: counter += 1
    return counter



f = open("D:\Documents\AoCinputs\inputday2a.txt")
lista = list(map(lambda x: x.rstrip(), f.readlines()))
print(counterA(lista))
print(counterB(lista))
