import math

liczba1 = int(input("Podaj pierwszą liczę"))
liczba2 = int(input("Podaj drugą liczbę"))
liczba3 = int(input("Podaj liczbę do spierwiastkowania"))

def sumowanie(x,y):
    print("Suma:"+str(x+y))
def odejmowanie(x,y):
    print("Różnica:"+str(x-y))
def iloczyn(x,y):
    print("Iloczyn:"+str(x*y))
def iloraz(x,y):
    print("Iloraz:"+str(x/y))
def pierwiastkowanie(x):
    print("Pierwiastek:"+str(math.sqrt(x)))
sumowanie(liczba1,liczba2)
odejmowanie(liczba1,liczba2)
iloczyn(liczba1,liczba2)
iloraz(liczba1,liczba2)
pierwiastkowanie(liczba3)
