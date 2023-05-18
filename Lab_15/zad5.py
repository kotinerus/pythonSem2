zajetetPokojeT=[]
wolnePokojeT=[['101', '102', '103', '104', '105', '106', '107', '108', '109', '110'],['201', '202', '203', '204', '205', '206', '207', '208', '209', '210'],['301', '302', '303', '304', '305', '306', '307', '308', '309', '310']]
class Hotel:
    def __init__(self,liczbaPokoi,pietra,liczbaKlientów,zajetePokoje,wolnePokoje):
        self.liczbaPokoi =liczbaPokoi
        self.pietra = pietra
        self.liczbaKlientów = liczbaKlientów
        self.zajetePokoje = zajetePokoje
        self.wolnePokoje = wolnePokoje


    def rezerwacjaPokoju(self,imieKlienta,nazwiskoKlienta,kod):

        if self.wolnePokoje == 0:
            print("Nie ma wolnych pokoi")
        else:
            wyborPietra = input(f'Na jakim piętrze chcesz mieć pokój?\n1: Piętro pierwsze [{10-len(wolnePokojeT[0])}/10]\n2: Piętro drugie [{10-len(wolnePokojeT[1])}/10]\n3: Piętro trzecie [{10-len(wolnePokojeT[2])}/10]\nWybór: ')
            match wyborPietra:
                case '1':
                    print(wolnePokojeT[0])
                    wyborPokoju = input("Wybieram pokój numer: ")
                    del wolnePokojeT[0][(wolnePokojeT[0].index(wyborPokoju))]
                case '2':
                    print(wolnePokojeT[1])
                    wyborPokoju = input("Wybieram pokój numer: ")
                    del wolnePokojeT[0][wolnePokojeT[1].index(wyborPokoju)]
                case '3':
                    print(wolnePokojeT[2])
                    wyborPokoju = input("Wybieram pokój numer: ")
                    del wolnePokojeT[0][wolnePokojeT[2].index(wyborPokoju)]
                case _:
                    print("Pomyliłeś się. Spróbuj ponownie.")
            zajetetPokojeT.append([kod, wyborPokoju])
            print(f'Pokój {wyborPokoju} został zarezerowany przez {imieKlienta} {nazwiskoKlienta}')
    def zwolnijPokoj(self,identyfikator,numerPokoju,atrybut):
        for i in zajetetPokojeT:
            if(atrybut=='a'):
                if(identyfikator==i[0]):
                    del zajetetPokojeT[i]
                    print(f'Pokoje użytkownika o indeksie {identyfikator} zostały zwolnione')
            else:
                if(identyfikator==i[0] and numerPokoju==i[1]):
                    del zajetetPokojeT[i]
                    print(f'Pokój {numerPokoju} został zwolniony')


class Klient:
    def __init__(self,imie,nazwisko,identyfikatorKlienta):
        self.imie = imie
        self.nazwisko = nazwisko
        self.identyfikatorKlienta = identyfikatorKlienta

pierwszyHotel = Hotel(310,3,0,zajetetPokojeT,wolnePokojeT)
klient1 = Klient("Krzysztof",'Wysocki','#001')
pierwszyHotel.rezerwacjaPokoju(klient1.imie,klient1.nazwisko,klient1.identyfikatorKlienta)
pierwszyHotel.zwolnijPokoj('#001','330','a')
