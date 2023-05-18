import datetime
import random


class samochod:
    def __init__(self,marka,rodzaj,przebieg, kolor, przyspiesznie, spalanieNa100, wlasciciel):
        self.marka = marka
        self.rodzaj = rodzaj
        self.przebieg = przebieg
        self.kolor = kolor
        self.przyspieszenie = przyspiesznie
        self.spalanieNa100 = spalanieNa100
        self.wlasciciel = wlasciciel

    def zatrab(self):
        return ("{} robi: Beep!".format(self.marka))

    def przyspieszanie(self, predkoscP, predkoscK):
        predkoscPC = predkoscP*(1000/3600)
        predkoscKC = predkoscK * (1000 / 3600)
        czas = (predkoscKC-predkoscPC)/self.przyspieszenie
        return "Przyspieszyłem do {} w czasie {}".format(predkoscK,int(round(czas,0)))

    def drift(self, predkosc):
        szansa = random.randint(1,10)
        print("\nWchodzę w drift...")
        if(predkosc<80):
            if(szansa>=4):
                return "Drift udany"
            else:
                return "Drift nieudany. Skpończyłeś na drzewie"
        else:
            if (szansa >= 8):
                return "Drift udany"
            else:
                return "Drift nieudany. Skpończyłeś na drzewie"

    def kosztPrzejazdu(self, dlugoscTrasy):
        cena = 6.60
        return round((dlugoscTrasy/100)*self.spalanieNa100*cena,2)

    def wyslijWKosmos(self):
        if(self.wlasciciel=='Elon Musk'):
            return 'Twój samochód jest w kosmosie'
        else:
            return 'Twój samochód nie jest w kosmosie'




samochod1 = samochod('Ferrari','Kabriolet','60000','Czerwony',6, 7, 'Elon Musk')
samochod2 = samochod('Porsche','Supersamochód','160000','Zółta',4, 4, 'Walter White')
samochod3 = samochod('Mazda','SUV','20000','Czarna',2, 3, 'Jessie Pinkman')
samochod4 = samochod('Cupra','Hatchback','330000','Zielona',3, 9, 'Tommas Shelby')
samochod5 = samochod('Toyota','Sedan','700000','Różowa',5, 6, 'El Profesor')

print(samochod1.przyspieszanie(0,100))
print(samochod1.drift(120))
print(samochod1.wyslijWKosmos())
print(samochod1.zatrab())
print("Koszt przejazdu to {}".format(samochod1.kosztPrzejazdu(279)))
