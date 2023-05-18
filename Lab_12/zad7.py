def naRzymskie(x):
    l1 = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
    l2 = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    l3 = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    l4 = ['', 'M', 'MM', 'MMM', 'MV-', 'V-', 'V-M', 'V-MM', 'V-MMM', 'X-']
    liczba = []
    for idx, i in enumerate(reversed(str(x))):
        match (idx + 1):
            case 1:
                liczba.insert(0, l1[int(i)])
            case 2:
                liczba.insert(0, l2[int(i)])
            case 3:
                liczba.insert(0, l3[int(i)])
            case 4:
                liczba.insert(0, l4[int(i)])
            case _:
                print("Potrafię podać maksymalnie liczbę 4-cyfrową")
    print("Liczba {} w rzymskich to: {}".format(x, ''.join(liczba)))


def zRzymskich(x):
    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    lista = []
    for i in range(len(x)):
        if (i == (len(x) - 1)):
            if (dict[x[i - 1]] < dict[x[i]]):
                pass
            else:
                lista.append(dict[x[i]])
        else:
            if (dict[x[i]] < dict[x[i + 1]]):
                lista.append(dict[x[i + 1]] - dict[x[i]])
                i += 1
            else:
                lista.append(dict[x[i]])
    for j in range(len(lista)):
        try:
            if(lista[j+1]>lista[j]):
                del lista[j+1]
        except IndexError:
            pass
    print("Liczba {} to: {}".format(x, sum(lista)))


liczba = int(input("Podaj liczbę w systemie dziesiętnym: "))
naRzymskie(liczba)
liczbaR = input("Podaj liczbę rzymską: ")
zRzymskich(liczbaR)
