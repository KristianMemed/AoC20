def find2020a(myList):
    for i in range(len(myList)):
        for j in range(len(myList)-1, 0 , -1):
            if(myList[i]+myList[j] == 2020): 
                return myList[i]*myList[j]
            if(2020 - myList[i] < myList[j]): break
    return 0

def find2020b(myList):
    for i in range(len(myList)):
        for j in range(len(myList)-1, 0 , -1):
            if(2020 - myList[i] < myList[j]): break
            for k in range(len(myList)-1, 0 , -1):
                if(2020 - myList[i] - myList[j] < myList[k]): break
                if(myList[i]+myList[j]+myList[k] == 2020):
                    return myList[i]*myList[j]*myList[k]
    return 0

f = open("D:\Documents\AoCinputs\inputday1a.txt")
lista = list(map(int, f.readlines()))
lista.sort(reverse = True)
print('result a) = ', find2020a(lista))
print('result b) = ', find2020b(lista))
