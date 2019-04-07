import pytest

from piskvorky import tah, tah_pocitace, vyhodnot


def test_vyhodnot_vyhra_x():
    """
    Křížky vyhrály.
    """
    assert vyhodnot("xxx-----------------") == "x"
    assert vyhodnot("--------xxx---------") == "x"
    assert vyhodnot("-----------------xxx") == "x"
    assert vyhodnot("-xoxoxxxoxoxoxoxoxox") == "x"
    assert vyhodnot("-xooxxooxxooxxoxxxoo") == "x"
    assert vyhodnot("xxxoxoxoxoxoxoxoxox-") == "x"
    assert vyhodnot("oxxxoxoxxooxxooxxoo-") == "x"
    assert vyhodnot("oxoxoxoxo-oxoxoxoxxx") == "x"
    assert vyhodnot("xxooxxoox-ooxxooxxxo") == "x"

    assert vyhodnot("---xxx--------------") == "x"      #dopsaný test
    assert vyhodnot("------------xxx-----") == "x"      #dopsaný test


def test_vyhodnot_vyhra_o():
    """
    Kolečka vyhrála.
    """
    assert vyhodnot("ooo-----------------") == "o"
    assert vyhodnot("--------ooo---------") == "o"
    assert vyhodnot("-----------------ooo") == "o"
    assert vyhodnot("-xoxoxoxoooxoxoxoxox") == "o"
    assert vyhodnot("-xoooxooxxooxxooxxoo") == "o"
    assert vyhodnot("xoooxoxoxoxoxoxoxox-") == "o"
    assert vyhodnot("oooxxooxxooxxooxxoo-") == "o"
    assert vyhodnot("oxoxoxoxo-oxoxoxooox") == "o"
    assert vyhodnot("xxooxxoox-ooxxooxooo") == "o"

    assert vyhodnot("---ooo--------------") == "o"      #dopsaný test
    assert vyhodnot("------------ooo-----") == "o"      #dopsaný test


def test_vyhodnot_remiza():
    """
    Nastala remíza.
    """
    assert vyhodnot("oxoxoxoxoxoxoxoxoxox") == "!"
    assert vyhodnot("xxooxxooxxooxxooxxoo") == "!"

    assert vyhodnot("ooxxooxxooxxooxxooxx") == "!"      #dopsaný test
    assert vyhodnot("xoxoxoxoxoxoxoxoxoxo") == "!"      #dopsaný test

    assert vyhodnot("abcd") == "!"                      #dopsaný test




def test_vyhodnot_hra():
    """
    Hra neskončila.
    """
    assert vyhodnot("--------------------") == "-"
    assert vyhodnot("xx----------------oo") == "-"
    assert vyhodnot("-xoxoxoxoxoxoxoxoxox") == "-"
    assert vyhodnot("-xooxxooxxooxxooxxoo") == "-"
    assert vyhodnot("xoxoxoxoxoxoxoxoxox-") == "-"
    assert vyhodnot("xooxxooxxooxxooxxoo-") == "-"
    assert vyhodnot("oxoxoxoxo-oxoxoxoxox") == "-"
    assert vyhodnot("xxooxxoox-ooxxooxxoo") == "-"

    assert vyhodnot("----xxoox-ooxxooxxoo") == "-"      #dopsaný test
    assert vyhodnot("xxooxxoox-ooxx------") == "-"      #dopsaný test


def test_tah_x():
    """
    Pozitivní testy se symbolem "x".
    """
    assert tah("--------------------", 0, "x") == "x-------------------"
    assert tah("--------------------", 10, "x") == "----------x---------"
    assert tah("--------------------", 19, "x") == "-------------------x"

    assert tah("--------------------", 5, "x") == "-----x--------------"        #dopsaný test
    assert tah("--------------------", 18, "x") == "------------------x-"       #dopsaný test


def test_tah_o():
    """
    Pozitivní testy se symbolem "o".
    """
    assert tah("--------------------", 0, "o") == "o-------------------"
    assert tah("--------------------", 10, "o") == "----------o---------"
    assert tah("--------------------", 19, "o") == "-------------------o"

    assert tah("--------------------", 5, "o") == "-----o--------------"        #dopsaný test
    assert tah("--------------------", 18, "o") == "------------------o-"       #dopsaný test


def test_tah_pocitace_prazdne():
    """
    Hra na prázdné pole.
    """
    pole = "--------------------"
    symbol_pocitace = "o"
    result = tah_pocitace(pole,symbol_pocitace)
    assert len(result) == 20
    assert result.count("-") == 19
    assert result.count("o") == 1

    pole = "x-------------------"       #dopsaný test
    symbol_pocitace = "o"
    result = tah_pocitace(pole,symbol_pocitace)
    assert len(result) == 20
    assert result.count("-") == 18
    assert result.count("o") == 1

    pole = "-------------------x"       #dopsaný test
    symbol_pocitace = "o"
    result = tah_pocitace(pole,symbol_pocitace)
    assert len(result) == 20
    assert result.count("-") == 18
    assert result.count("o") == 1





def test_tah_pocitace_skoro_plne():
    """
    Hra na skoro plné pole (volno uprostřed).
    """
    pole = "xoxoxoxoxo-xoxoxoxox"
    symbol_pocitace = "o"
    result = tah_pocitace(pole,symbol_pocitace)
    assert len(result) == 20
    assert result.count("x") == 10
    assert result.count("o") == 10

    pole = "xoxoxoxox-oxoxoxoxox"       #dopsaný test
    symbol_pocitace = "o"
    result = tah_pocitace(pole,symbol_pocitace)
    assert len(result) == 20
    assert result.count("x") == 10
    assert result.count("o") == 10

    pole = "xoxoxoxoxox-oxoxoxox"       #dopsaný test
    symbol_pocitace = "o"
    result = tah_pocitace(pole,symbol_pocitace)
    assert len(result) == 20
    assert result.count("x") == 10
    assert result.count("o") == 10


def test_tah_pocitace_skoro_plne_zacatek():
    """
    Hra na skoro plné pole (volno na začátku).
    """
    pole = "-xoxoxoxoxoxoxoxoxox"
    symbol_pocitace = "o"
    result = tah_pocitace(pole,symbol_pocitace)
    assert len(result) == 20
    assert result.count("x") == 10
    assert result.count("o") == 10

    pole = "-oxxoxoxoxoxoxoxoxox"       #dopsaný test
    symbol_pocitace = "o"
    result = tah_pocitace(pole,symbol_pocitace)
    assert len(result) == 20
    assert result.count("x") == 10
    assert result.count("o") == 10

    pole = "-xoxoxoxoxoxoxoxoxxo"       #dopsaný test
    symbol_pocitace = "o"
    result = tah_pocitace(pole,symbol_pocitace)
    assert len(result) == 20
    assert result.count("x") == 10
    assert result.count("o") == 10




def test_tah_pocitace_skoro_plne_konec():
    """
    Hra na skoro plné pole (volno na konci).
    """
    pole = "xoxoxoxoxoxoxoxoxox-"
    symbol_pocitace = "o"
    result = tah_pocitace(pole,symbol_pocitace)
    assert len(result) == 20
    assert result.count("x") == 10
    assert result.count("o") == 10

    pole = "xxooxoxoxoxoxoxoxox-"       #dopsaný test
    symbol_pocitace = "o"
    result = tah_pocitace(pole,symbol_pocitace)
    assert len(result) == 20
    assert result.count("x") == 10
    assert result.count("o") == 10

    pole = "xxooxoxoxoxoxoxooxx-"       #dopsaný test
    symbol_pocitace = "o"
    result = tah_pocitace(pole,symbol_pocitace)
    assert len(result) == 20
    assert result.count("x") == 10
    assert result.count("o") == 10


def test_tah_pocitace_skoro_plne_konec_2():
    """
    Hra na skoro plné pole (2× volno na konci).
    """
    pole = "xooxxooxoxoxoxooxx--"
    symbol_pocitace = "o"
    result = tah_pocitace(pole,symbol_pocitace)
    assert len(result) == 20
    assert result.count("x") == 9
    assert result.count("o") == 10
    assert result.count("-") == 1

    pole = "oxoxxooxoxoxoxooxx--"       #dopsaný test
    symbol_pocitace = "o"
    result = tah_pocitace(pole,symbol_pocitace)
    assert len(result) == 20
    assert result.count("x") == 9
    assert result.count("o") == 10
    assert result.count("-") == 1

    pole = "xooxxooxoxoxoxoxox--"       #dopsaný test
    symbol_pocitace = "o"
    result = tah_pocitace(pole,symbol_pocitace)
    assert len(result) == 20
    assert result.count("x") == 9
    assert result.count("o") == 10
    assert result.count("-") == 1

def test_jina_delka_pole_tah_pocitac():     #test na jinou délku pole
    delkapole=2
    pole=delkapole*"-"
    symbol_pocitace = "o"
    result = tah_pocitace(pole,symbol_pocitace)
    assert len(result) == delkapole
    assert result.count("-") == delkapole-1
    assert result.count("o") == 1

def test_plne_hraci_pole_tah_pocitac():     #test na plné pole
    with pytest.raises(ValueError):
        pole = "xoxoxoxxoxoxx"
        symbol_pocitace = "o"
        result = tah_pocitace(pole,symbol_pocitace)

def test_nulove_hraci_pole():       #test na prázné pole
    with pytest.raises(ValueError):
        pole = ""
        symbol_pocitace = "o"
        result = tah_pocitace(pole,symbol_pocitace)





if __name__ == "__main__":
    pytest.main()
