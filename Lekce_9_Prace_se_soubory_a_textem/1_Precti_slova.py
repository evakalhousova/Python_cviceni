# Vytvoř program, který přečte textový soubor a zobrazí slova, která obsahují 7 a více znaků.
# Jednotlivé kroky, které program musí obsahovat:
# Vytvoř si složku, vytvoř v ní soubor slova.txt a main.py,             # Místo main.py používám 1_Precti_slova.py
# do souboru slova.txt ulož následující slova:
# koupelna
# zona
# syr
# teta
# kriz
# rodina
# nacitani
# cokolada
# asociace
# lavicka
# povrch
# rotace
# zamestnanec
# balicek
# komunikace
# popularni
# veta
# v souboru main.py, vytvoř funkci zobraz_slova, která bude mít jeden parameter textovy soubor,
# funkce zobraz_slova vezme soubor, přečte jeho obsah a vypíše všechny slova, která obsahují 7 a více znaků.
# Ukázka průběhu
# koupelna nacitani cokolada asociace lavicka zamestnanec balicek komunikace popularni


# Prvně jsem si procvičovala vytváření složek a souborů, samotné řešení úkolu je níže:
import os

def vytvor_slozku():
    path = f'C:/Python/Projekt_1/Lekce_9_Prace_se_soubory_a_textem/Ukol'
    if not os.path.isdir(path):
        os.mkdir(path)

seznam = [
    'koupelna',             # Ctrl + Shift + šipka dolů (zduplikuje kurzor), pak dopsat uvozovku, pak End, pak dopsat uvozovku a čárku.
    'zona',
    'syr',
    'teta',
    'kriz',
    'rodina',
    'nacitani',
    'cokolada',
    'asociace',
    'lavicka',
    'povrch',
    'rotace',
    'zamestnanec',
    'balicek',
    'komunikace',
    'popularni',
    'veta',
]

novy_seznam = []
for polozka in seznam:
    novy_seznam.append(polozka + '\n')

def vytvor_soubor_se_seznamem():
    with open(f'{path}/slova.txt', mode='w') as txt_soubor:
        txt_soubor.writelines(novy_seznam)


# Tady teprve začíná začíná řešení úkolu:
def zobraz_slova(textovy_soubor: str):
    with open(textovy_soubor, mode='r') as f:
        txt_obsah = f.readlines()
    sedm_pismen = []
    for radek in txt_obsah:
        strip_radek = radek.strip('\n')
        if len(strip_radek) >= 7:
            sedm_pismen.append(strip_radek)
        else:
            continue
    return sedm_pismen

print(zobraz_slova('C:/Python/Projekt_1/Lekce_9_Prace_se_soubory_a_textem/slova.txt'))


# Jiné řešení (Engeto):
def zobraz_slova(textovy_soubor):
    """
    Vytvor funkci, ktera otevre textovy soubor a precte slova.
    """
    zadana_slova = open(textovy_soubor, "r")
    data = zadana_slova.read()
    slova = data.split()
    for slovo in slova:
        if len(slovo) >= 7:
            print(slovo, end=" ")
    zadana_slova.close()

if __name__ == "__main__":
    zobraz_slova("slova.txt")
