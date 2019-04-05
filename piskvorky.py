from random import randrange
from ai import tah_pocitace
from util import tah


def vyhodnot(pole):
    "Vyhodnotí stav pole."
    if 'xxx' in pole:
        return("x")
    elif 'ooo' in pole:
        return("o")
    elif '-' not in pole:
        return("!")
    else:
        return '-'



def tah_hrace(herni_pole):
    "Ptá se hráče na kterou pozici chce hrát a vrací herní pole se zaznamenaným tahem"

    while True:
        cislo_pozice = int(input("Na kterou pozici chceš hrát? "))
        if cislo_pozice >= 0 and cislo_pozice < len(herni_pole) and herni_pole[cislo_pozice] == "-":
            return tah(herni_pole, cislo_pozice, "x")
        else:
            print("Špatná pozice, zkus to znovu. ")


def piskvorky(delkapole,symbol_pocitace):
    "Vygeneruje prázdné pole a střídá tah hráče a počítače. "
    pole = "-"*delkapole
    while True:
        print(pole)
        pole = tah_hrace(pole)
        print(pole)
        if "-" not in pole:
            raise ValueError('Máš plné hrací pole')
        pole = tah_pocitace(pole,symbol_pocitace)
        if vyhodnot(pole) != '-':
            break

    print(pole)
    if vyhodnot(pole) == '!':
        print('Remíza!')
    elif vyhodnot(pole) == 'x':
        print('Vyhrála jsi!')
    elif vyhodnot(pole) == 'o':
        print('Vyhrál počítač!')

# piskvorky()
