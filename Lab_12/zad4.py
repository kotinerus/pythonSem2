liczba1 = int(input("Podaj pierwszą liczbę: "))
liczba2 = int(input("Podaj drugą liczbę: "))

def lecimy(x):
    if(x<5.0):
        print("{}km to za nisko".format(x))
    else:
        print("Na tej wysokości jesteśmy bezpieczni")
lecimy(liczba1)