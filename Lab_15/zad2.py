class Sklep:
    def __init__(self,nazwa,artykuly):
        self.nazwa = nazwa
        self.artykuly = artykuly

    def sortujArytkuly(self):
        print(self.artykuly)
class Beer:
    def __init__(self,nazwa,stezenieAlkoholu,cena,kategoria,opinia):
        self.nazwa = nazwa
        self.stezenieAlkoholu = stezenieAlkoholu
        self.cena = cena
        self.kategoria = kategoria
        self.opinia = opinia

class PiwoBezalkoholowe(Beer):
    def __init__(self,nazwa,cena,opinia):
        super().__init__(nazwa,0,cena,"Bezalkoholowe",opinia)

class PiwoAlkoholowe(Beer):
    def __init__(self,nazwa,stezenie,cena,opinia):
        super().__init__(nazwa,stezenie,cena,"Alkoholowe",opinia)

lechFree1 = PiwoBezalkoholowe("Lech Free",4.89,4)
lechFree2 = PiwoBezalkoholowe("Lech Free Arbuz I Mięta",4.99,5)
heineken1 = PiwoAlkoholowe("Heineken",5.0,4.39,3)
snajper = PiwoAlkoholowe("Snajper",12,4.49,1)
kustosz = PiwoAlkoholowe("Kustosz Mocne",6.5,2.29,2)

sklep1 = Sklep("Kangur",[lechFree1,lechFree2,heineken1,snajper,kustosz])
sklep1.sortujArytkuly()

