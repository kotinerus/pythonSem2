import random


class Restaurant:
    def __init__(self, nameOfRestaurant):
        self.nameOfRestaurant = nameOfRestaurant

class IceCreamStand(Restaurant):
    def __init__(self,nameOfRestaurant,flavours):
        super().__init__(nameOfRestaurant)
        self.flavours = flavours

    def showFlavours(self):
        for i in range(len(self.flavours)):
            if i == 0:
                print("- - - - - - - - - - - -\n| " + self.flavours[i] + "\n- - - - - - - - - - - -")
            elif i == len(self.flavours) - 1:
                print("| " + self.flavours[i] + "\n- - - - - - - - - - - -")
            else:
                print("| " + self.flavours[i] + "\n- - - - - - - - - - - -")
        return 0

class CoffeeShop(Restaurant):
    def __init__(self,nameOfRestaurant,typesOfCoffe):
        super().__init__(nameOfRestaurant)
        self.typesOfCoffe = typesOfCoffe

    def showCoffes(self):
        for i in range(len(self.typesOfCoffe)):
            if i == 0:
                print("- - - - - - - - - - - -\n| " + self.typesOfCoffe[i] + "\n- - - - - - - - - - - -")
            elif i == len(self.typesOfCoffe) - 1:
                print("| " + self.typesOfCoffe[i] + "\n- - - - - - - - - - - -")
            else:
                print("| " + self.typesOfCoffe[i] + "\n- - - - - - - - - - - -")
        return 0

    def ocenaZadowolenia(self):
        wybranaKawa = self.typesOfCoffe[random.randint(0,len(self.typesOfCoffe))]
        zadowolenieKlienta=random.randint(1,100)
        print ("Klient zamówił {} i był zadowolony w {}%".format(wybranaKawa,zadowolenieKlienta))
sklepZKawa1 = CoffeeShop("Wielbłąd",['Black','Latte','Cappuccino','Americano','Espresso','Doppio'])
sklepZKawa1.showCoffes()
sklepZLodami1 = IceCreamStand("Pod Strusiem", ['Czekoladowe','Truskawkowe','Waniliowe'])
sklepZLodami1.showFlavours()
sklepZKawa1.ocenaZadowolenia()