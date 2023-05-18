import random

bratAlbert = []
joachim = []
kartyNaStole = []
wynikStoluW = 0
dostepneKarty = []


class Talia():
    def __init__(self):
        self.iloscKart = 52
        self.kolor = ['Pik', 'Kier', 'Trefl', 'Karo']
        self.wartosc = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']

    def dodawanieKartDoTali(self):
        for kolor in self.kolor:
            for wartosc in self.wartosc:
                dostepneKarty.append([kolor, wartosc])

    def usuniecieKartyZTali(self, kolorKarty, wartoscKarty):
        valueKolor = self.kolor.index(kolorKarty)
        valueWartosc = self.wartosc.index(wartoscKarty)
        pozycja = valueKolor * 13 + valueWartosc
        del dostepneKarty[pozycja]
        print(f'* * * * * *\nUsunąłem kartę |{kolorKarty.capitalize()} {wartoscKarty.capitalize()}|\n* * * * * *')

    def rozdanieKart(self, player):
        for i in range(2):
            karta = random.randint(0, len(dostepneKarty) - 1)
            player.append(dostepneKarty[karta])
            del dostepneKarty[karta]

    def pokazKarty(self):
        counter = 0
        for index, karta in enumerate(dostepneKarty):
            print(karta, end="")
            counter += 1
            if (counter == 13):
                print('')
                counter = 0

    def kartyStol(self):
        for i in range(5):
            war = len(dostepneKarty)
            karta = random.randint(0, len(dostepneKarty) - 1)
            kartyNaStole.append(dostepneKarty[karta])
            dostep = len(dostepneKarty)
            del dostepneKarty[karta]

    def sumaNaStole(self):
        wynikStolu=0
        for i, j in kartyNaStole:

            match j:
                case 'A':
                    wynikStolu += 14
                case 'K':
                    wynikStolu += 13
                case 'Q':
                    wynikStolu += 12
                case 'J':
                    wynikStolu += 11
                case _:
                    wynikStolu += j
        return wynikStolu
    def wynikUser(self,user):
        wynikUsera=0
        for i, j in user:

            match j:
                case 'A':
                    wynikUsera += 14
                case 'K':
                    wynikUsera += 13
                case 'Q':
                    wynikUsera += 12
                case 'J':
                    wynikUsera += 11
                case _:
                    wynikUsera += j
        return wynikUsera

    def ktoWygral(self):
        if(wynikJoachim>wynikbratAlbert):
            print("Wygrał Joachim")
        else:
            print('Wygrał brat Albert')

element = Talia()
element.dodawanieKartDoTali()
element.kartyStol()
element.rozdanieKart(bratAlbert)
element.rozdanieKart(joachim)
element.usuniecieKartyZTali("Trefl", 'K')
wynikStoluW=element.sumaNaStole()
wynikJoachim = wynikStoluW+element.wynikUser(joachim)
wynikbratAlbert = wynikStoluW+element.wynikUser(bratAlbert)
element.ktoWygral()

