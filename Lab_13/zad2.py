import random

ksiazkiNapolce = []

class ksiakza:
    def __init__(self, tytul, autor, rokWydania, gatunek, iloscStron, pozycjaNaPolce, wydanie):
        self.tytul = tytul
        self.autor = autor
        self.rokWydania = rokWydania
        self.gatunek = gatunek
        self.iloscStron = iloscStron
        self.pozycjaNaPolce = pozycjaNaPolce
        self.wydanie = wydanie

    def przeczytajCala(self):
        print("Przeczytanie tej książki zajmie około {} godzin. Kontynuować?(tak/nie): ".format(round(self.iloscStron/35),2))
        decyzja = input()
        if decyzja=='tak':
            return "Przeczytałem"
        else:
            return "Nie przeczytałem"

    def autorKobieta(self):
        autor = self.autor.split(" ")
        if(autor[0][-1]=='a'):
            return "Autor to kobieta"
        else:
            return "Autor to mężczyzna"

    def odlozNaPolke(self):
        decyzja = input("Chcesz położyć książkę na stole czy na półce?")
        if(decyzja=='stole'):
            return "Położuyłem książkę na stole"
        else:
            return "Położyłem książkę na półce. Jej pozycja to {}".format(self.pozycjaNaPolce)

    def uderzenie(self):
        if(self.wydanie=='twarde'):
            return "Uderzenie będzie bolało"
        else:
            return "Nie poczujesz uderzenia"

    def czytanie(self):
        for i in range(self.iloscStron):
            print('Czytam stronę '+str(i))
        return "Najciekawsza była strona {}".format(random.randint(1,self.iloscStron))


ksiakza1 = ksiakza("Folwark zwierzęcy","George Orwel",1943,'Powieść',132,7,'miekkie')
ksiakza2 = ksiakza("Czarna owca medycyny","Lieberman Jeffrey A.",2020,'Książka naukowa',288,1,'twarde')
ksiakza3 = ksiakza("Kontrakt","Balicka Joanna",2022,'Powieść',473,3,'miekkie')
ksiakza4 = ksiakza("Mężczyzna imieniem Ove","Backman Fredrik",2022,'Dramat',351,2,'twarde')
ksiakza5 = ksiakza("A Million Kisses in Your Lifetime","Murphy Monica",1945,'Dramat',544,5,'miekkie')


ksiazkiNapolce.append(ksiakza1)
ksiazkiNapolce.append(ksiakza2)
ksiazkiNapolce.append(ksiakza3)
ksiazkiNapolce.append(ksiakza4)
ksiazkiNapolce.append(ksiakza5)


lista = sorted(ksiazkiNapolce, key = lambda x: x.rokWydania, reverse=False)

#print(ksiakza1.przeczytajCala())
#print(ksiakza1.autorKobieta())
#print(ksiakza1.odlozNaPolke())
#print(ksiakza1.uderzenie())
#print(ksiakza1.czytanie())