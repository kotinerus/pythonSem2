import math

liczba1 = int(input("Podaj promień: "))
liczba2 = int(input("Podaj wysokość"))

def kula(r):
    pole = 4 * math.pi * (r**2)
    objetosc = 4/3 * math.pi * (r**3)
    print("Pole kuli to: {} \nObjętość kuli to: {} ".format(pole,objetosc))
def stozek(r,wysokosc):
    pole = 1/3 * math.pi * (r ** 2) * wysokosc
    objetosc = 1 / 3 * math.pi * (r ** 2) * wysokosc
    print("Pole stożka to: {} \nObjętość stożka to: {} ".format(pole, objetosc))
def szescian(r):
    pole = 6*(r**2)
    objetosc = r**3
    print("Pole sześcianu to: {} \nObjętość sześcianu to: {} ".format(pole, objetosc))

kula(liczba1)
stozek(liczba1,liczba2)
szescian(liczba1)
