def binarnie(x):
    print(bin(x)[2:])
def szesnastkowo(x):
    print(oct(x)[2:])

def binHex(x):
    dlugX = len(str(x))
    tablica = []
    liczbaTab=[]
    slowo = ''
    while dlugX>0:
        if dlugX>=4:
            odc=(str(x)[-4:])
            x=(str(x)[0:-4])
            dlugX=len(str(x))
            tablica.insert(0,odc)
        else:
            tablica.insert(0,x)
            dlugX=0
    for i in reversed(tablica):
        pot = 0
        sumowanie = []
        for j in reversed(i):
            if(j=='1'):
                sumowanie.append(2 ** pot)
            pot += 1
        liczba =sum(sumowanie)
        match liczba:
            case 10:
                liczbaTab.insert(0,"A")
            case 11:
                liczbaTab.insert(0, "B")
            case 12:
                liczbaTab.insert(0, "C")
            case 13:
                liczbaTab.insert(0, "D")
            case 14:
                liczbaTab.insert(0, "E")
            case 15:
                liczbaTab.insert(0, "F")
            case _:
                liczbaTab.insert(0, str(liczba))

    for x in range(len(liczbaTab)):
        slowo+=liczbaTab[x]
    print(slowo)
    
binHex(1001010111100) #Bardzo pogmatwane, ale nudziło mi się
liczbaWDec=int(input("Podaj liczę w systemie dziesiątkowym:"))
binarnie(liczbaWDec)
szesnastkowo(liczbaWDec)