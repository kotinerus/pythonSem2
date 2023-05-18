import random


class Zwierze:
    def __init__(self,wiek,kolor,gatunek,plec):
        self.wiek = wiek
        self.kolor = kolor
        self.gatunek = gatunek
        self.plec = plec

    def zdefiniujWiek(self):
        if(self.wiek<=1):
            return "Jestem nowy na tym świecie"
        elif self.wiek<=8:
            return "Trochę już żyję"
        elif self.wiek>8:
            return "Jestem staruszkiem"
        else:
            return "Błąd. Podana wartość jest nieprawidłowa"


class Kot(Zwierze):
    def __init__(self,wiek,kolor,plec):
        super().__init__(wiek,kolor,"Kot",plec)

    def spij(self):
        i=0
        while i<100:
            print("Śpię")
            i+=10
        print("Czas obudzić innych")

class Pies(Zwierze):
    def __init__(self,wiek,kolor,plec):
        super().__init__(wiek,kolor,"Pies",plec)

    def gonOgon(self):
        energia = random.randint(1,50)
        while energia>0:
            print("Gonię ogon!")
            energia-=random.randint(1,5)
        print("Idę spać")

class Ptak(Zwierze):
    def __init__(self,wiek,kolor,plec,predkoscLotu):
        super().__init__(wiek,kolor,"Ptak",plec)
        self.predkoscLotu = predkoscLotu

    def przelot(self,odleglosc):
        while odleglosc>0:
            print("Lecę. Będę tam za {}".format(round(odleglosc/self.predkoscLotu)))
            odleglosc-=self.predkoscLotu
        print("Doleciałem")
class Ryba(Zwierze):
    def __init__(self,wiek,kolor,plec):
        super().__init__(wiek,kolor,"Ryba",plec)

    def bulbul(self):
        print("Bul bul bul")

ptak1 = Ptak(10,"Czarny","Samiec",30)
ptak1.przelot(50)
pies1 = Pies(5,"Biały","samica")
pies1.gonOgon()