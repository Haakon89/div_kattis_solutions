antall=int(input())
dager=0
treD_printere=1
statuer=0
while statuer<antall:
    if treD_printere>=antall:
        statuer+=treD_printere
        dager+=1
    else:
        treD_printere+=1*treD_printere
        dager+=1
print(dager)


    