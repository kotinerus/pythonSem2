dlugosc = int(input("Podaj długość w stopach: "))

def zmiana(x):
    nametry = x*0.3048
    nacentymetry=nametry*100
    namilimetry=nametry*1000
    nakilometry=nametry/1000
    print("Długość w metrach: {}\nDługość w centymetrach: {}\nDługość w milimetrach: {}\nDługość w kilometrach: {}\n".format(nametry,nacentymetry,namilimetry,nakilometry))
zmiana(dlugosc)