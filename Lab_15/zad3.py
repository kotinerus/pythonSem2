#imie,nazwisko,ulica,numerDomu,kodPocztowy,miejscowość

class Obywatel():
    def __init__(self):
        self.imie = input("Podaj imię: ")
        self.nazwisko = input("Podaj nazwisko: ")
        self.ulica = input("Podaj ulice: ")
        self.numerDomu = input("Podaj numer domu: ")
        self.kodPocztowy = input("Podaj kod pocztowy:")
        self.miejscowosc = input("Podaj miejscowość:")
    def wizytowka(self):
        with open('wizytowka.txt', 'w') as file:
            file.write('----------------------\n')
            file.write(f'{self.imie} {self.nazwisko}\n')
            file.write(f'{self.ulica} {self.numerDomu}\n')
            file.write(f'{self.kodPocztowy} {self.miejscowosc}\n')
            file.write('----------------------')



bruh = Obywatel()
bruh.wizytowka()