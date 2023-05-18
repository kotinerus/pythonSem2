import random


class student:
    def __init__(self, poziomNauki, lubiPiwo, poziomWyspania,przedmiotyDoZdania):
        self.poziomNauki = poziomNauki
        self.lubiPiwo = lubiPiwo
        self.poziomWyspania = poziomWyspania
        self.przedmiotyDoZdania = przedmiotyDoZdania

    def procesNauki(self):
        while self.poziomNauki<100:
            procentNauki = random.randint(1,20)
            self.poziomNauki+=procentNauki
            if(self.poziomNauki<=100):
                print("Poziom nauki:"+str(self.poziomNauki)+"%")
            else:
                print("Poziom nauki: 100%")
        self.idzSpac()
        return "Nauczyłeś się"

    def piciePiwa(self):
        if(self.lubiPiwo=='tak'):
            self.idzSpac()
            return "Wypiłeś {}".format(random.randint(2,10))
        else:
            self.idzSpac()
            return "Wypiłeś jedno piwko z kumplami"

    def idzSpac(self):
        self.poziomWyspania -= random.randint(20, 50)
        if(self.poziomWyspania<=0):
            print("-----------------------------")
            print("Jesteś zmęczony. Musisz się przespać!")
            self.poziomWyspania = 0
            while self.poziomWyspania<=100:
                print("Spanie: {}%".format(self.poziomWyspania))
                self.poziomWyspania+=random.randint(10,30)
            print("Spanie: 100%")
            return print("Wyspałeś się\n-----------------------------")

student1=student(0,'tak',23,5)
print(student1.procesNauki())
print(student1.piciePiwa())



