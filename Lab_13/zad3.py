class telefon:
    def __init__(self, numer, producent, model, kosztAbonamentu):
        self.numer = numer
        self.model = model
        self.kosztAbonamentu=kosztAbonamentu
        self.producent = producent

    def dzwonienie(self):
        numerTelefonu = input("Podaj numer na który chcesz zadzwonić")
        if(len(numerTelefonu)==9):
            for i in range(3):
                print('.'*(i+1))
            return "Nawiązałem połączenie z {}".format(numerTelefonu)

    def podajAbonament(self):
        print("Twój abonament wynosi {}".format(self.kosztAbonamentu))

    def czyJestesBogaty(self):
        if(self.producent=="Apple"):
            return "Fiu fiu, wydałeś sporo na telefon"
        else:
            return "Fiu fiu, dobrze gospodarujesz pieniezmi"

telefon1 = telefon( '754291853', 'Apple', 'IPhone X 128GB', '109,99zł')
print(telefon1.czyJestesBogaty())
