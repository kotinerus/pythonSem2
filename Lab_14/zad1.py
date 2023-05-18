class Pojazd:
    def __init__(self,nrTablicy,typPojazdu,rokProduckji):
        self.nrTablic =nrTablicy
        self.typPojazdu = typPojazdu
        self.rokProduckji = rokProduckji

class Samochód(Pojazd):
    def __init__(self,rokProduckji,nrTablicy,kolor):
        super().__init__(nrTablicy,"samochod",rokProduckji)
        self.kolor = kolor
    def czymJestem(self):
        print("Jestem {}em z roku {} o numerze tablicy {} i kolorze {}".format(self.typPojazdu,self.rokProduckji,self.nrTablic,self.kolor))

    def __del__(self):
        print("Usunięto")


class Motocykl(Pojazd):
    def __init__(self,rokProduckji,nrTablicy,kolor):
        super().__init__(nrTablicy,"motocykl",rokProduckji)
        self.kolor = kolor
    def czymJestem(self):
        print("Jestem {}em z roku {} o numerze tablicy {} i kolorze {}".format(self.typPojazdu,self.rokProduckji,self.nrTablic,self.kolor))

    def __del__(self):
        print("Usunięto")

motocykl1 = Motocykl(2012,'DW 193BC', 'czarnym')
motocykl1.czymJestem()
samochod1 = Samochód(1997,"DX 153TH", 'czerwonym')
samochod1.czymJestem()
