import re
noMandatoryFields = 7
noOptionalFields = 1

def checkPassports(myList):
    counter = 0
    mandatoryFields = 0
    optionalFields = 0
    for i in myList:
        if "byr" in i: mandatoryFields += 1
        if "iyr" in i: mandatoryFields += 1
        if "eyr" in i: mandatoryFields += 1
        if "hgt" in i: mandatoryFields += 1
        if "hcl" in i: mandatoryFields += 1
        if "ecl" in i: mandatoryFields += 1
        if "pid" in i: mandatoryFields += 1
        if "cid" in i: optionalFields += 1
        if not i: 
            if mandatoryFields == noMandatoryFields:
                counter += 1
            mandatoryFields = 0
            optionalFields = 0
    if mandatoryFields == noMandatoryFields:
                counter += 1
    return counter

def checkPassportsFull(myList):
    counter = 0;
    mandatoryFields = 0
    optionalFields = 0
    for i in myList:
        if not i: 
            if mandatoryFields == noMandatoryFields:
                counter += 1
            mandatoryFields = 0
            optionalFields = 0
            continue
        line = i.split(" ")
        for j in line:
            id = j.split(":")[0]
            code = j.split(":")[1]
            if "byr" == id and len(code) == 4 and int(code) >= 1920 and int(code) <= 2002 : mandatoryFields += 1
            if "iyr" == id and len(code) == 4 and int(code) >= 2010 and int(code) <= 2020 : mandatoryFields += 1
            if "eyr" == id and len(code) == 4 and int(code) >= 2020 and int(code) <= 2030 : mandatoryFields += 1
            if "hgt" == id:
               if "in" in code:
                   code = code.split("in")[0]
                   if int(code) >= 59 and int(code) <= 76:
                        mandatoryFields += 1
               if "cm" in code:
                    code = code.split("cm")[0]
                    if int(code) >= 150 and int(code) <= 193:
                        mandatoryFields += 1
            if "hcl" == id and len(code) == 7 and re.search('#[0-9a-f]{6}', code): mandatoryFields += 1
            if "ecl" == id and (code == "amb" or code == "blu" or code == "brn" or code == "gry" or code == "grn" or code == "hzl" or code == "oth"): mandatoryFields += 1
            if "pid" == id and len(code) == 9: mandatoryFields += 1
            if "cid" == id: optionalFields += 1
    if mandatoryFields == noMandatoryFields:
               counter += 1
               mandatoryFields = 0
               optionalFields = 0
    return counter


f = open("D:\Documents\AoCinputs\inputday4a.txt")
lista = list(map(lambda x: x.rstrip(), f.readlines()))
print(checkPassports(lista))
print(checkPassportsFull(lista))