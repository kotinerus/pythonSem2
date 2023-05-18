masa = int(input("Podaj swoją masę: "))
wysokosc = int(input("Podaj swój wzrost: "))

def BMI(x,y):
    cmNaM=y/100
    jakieBMI = x/(cmNaM**2)
    if(jakieBMI>25.0):
        print("Masz nadwagę")
    elif(25>jakieBMI>18.5):
        print("Twoja waga jest prawidłowa")
    else:
        print ("Masz niedowagę")

BMI(masa, wysokosc)