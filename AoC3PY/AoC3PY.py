def treeHits(m, n):
    counter = 0
    k = 0
    noSkips = 0
    for i in lista:
        if noSkips > 1: 
            noSkips -=1
            continue
        if i[k] == '#': counter+=1
        k += m
        k = k % len(i)
        if n > 1 : noSkips = n
    return counter


f = open("D:\Documents\AoCinputs\inputday3a.txt")
lista = list(map(lambda x: x.rstrip(), f.readlines()))
no11 = treeHits(1, 1)
no31 = treeHits(3, 1)
no51 = treeHits(5, 1)
no71 = treeHits(7, 1)
no12 = treeHits(1, 2)

print(no11 * no31 * no51 * no71 * no12)