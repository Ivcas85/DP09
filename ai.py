from random import randrange
from util import tah

def tah_pocitace(herni_pole,symbol_pocitace):
    "Vrátí herní pole se zaznamenaným tahem počítače. "
    if "-" not in herni_pole:
        raise ValueError('Máš plné hrací pole')
    elif len(herni_pole) <=0:
        raise ValueError('Délka pole musí být větší než 0')
    while True:
        cislo_pozice = randrange(len(herni_pole))
        if herni_pole[cislo_pozice] == "-":
            symbol=symbol_pocitace
            return tah(herni_pole, cislo_pozice,symbol)
