import math


class Figura:
    def __init__(self,iloscKrawedzi,iloscWierzchołków):
        self.iloscKrawedzi = iloscKrawedzi
        self.iloscWierzchołków = iloscWierzchołków

class Kwadrat(Figura):
    def __init__(self,dlugoscKrawedzi):
        super().__init__(4,4)
        self.dlugoscKrawedzi = dlugoscKrawedzi

    def Pole(self):
        return self.dlugoscKrawedzi**2

    def Obwod(self):
        return self.dlugoscKrawedzi*4

class Prostokat(Figura):
    def __init__(self,dlguoscKrawedziA,dlguoscKrawedziB):
        super().__init__(4,4)
        self.dlguoscKrawedziA = dlguoscKrawedziA
        self.dlguoscKrawedziB = dlguoscKrawedziB

    def Pole(self):
        return self.dlguoscKrawedziB*self.dlguoscKrawedziA

    def Obwod(self):
        return self.dlugoscKrawedziA*2+self.dlguoscKrawedziB*2

class Trojkat(Figura):
    def __init__(self,dlugoscKrawedziA,dlugoscKrawedziB,dlugoscKrawedziC, wysokosc):
        super().__init__(3,3)
        self.dlugoscKrawedziA = dlugoscKrawedziA
        self.dlugoscKrawedziB = dlugoscKrawedziB
        self.dlugoscKrawedziC = dlugoscKrawedziC
        self.wysokosc = wysokosc

    def Pole(self):
        return (self.dlugoscKrawedziA*self.wysokosc)/2
    def Obwod(self):
        return  self.dlugoscKrawedziA+self.dlugoscKrawedziB+self.dlugoscKrawedziC
class Kolo(Figura):
    def __init__(self, promien):
        super().__init__(0, 0)
        self.promien = promien

    def Pole(self):
        return self.promien**2*math.pi
    def Obwod(self):
        return 2*math.pi*self.promien
class Romb(Figura):
    def __init__(self, dlugoscPrzekatnejA, dlugoscPrzekatnejB, dlugoscA, dlugoscB ):
        super().__init__(4, 4)
        self.dlugoscPrzekatnejA = dlugoscPrzekatnejA
        self.dlugoscPrzekatnejB = dlugoscPrzekatnejB
        self.dlugoscA = dlugoscA
        self.dlugoscB = dlugoscB

    def Pole(self):
        return self.dlugoscPrzekatnejA*self.dlugoscPrzekatnejB/2
    def Obowod(self):
        return 2*self.dlugoscA+2*self.dlugoscB
class Trapez(Figura):
    def __init__(self, wysokosc, dlugoscA, dlugoscB,dlugoscC,dlugoscD ):
        super().__init__(4, 4)
        self.wysokosc = wysokosc
        self.dlugoscA = dlugoscA
        self.dlugoscB = dlugoscB
        self.dlugoscC = dlugoscC
        self.dlugoscD = dlugoscD

    def Pole(self):
        return (self.dlugoscA+self.dlugoscB * self.wysokosc) /2
    def Obowod(self):
        return self.dlugoscA+self.dlugoscB+self.dlugoscC+self.dlugoscD