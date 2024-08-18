# Vytvoř program, který ze zadaného listu vytáhne emaily, které obsahují čísla.
# Tvoje úloha musí obsahovat tyto kroky:
# Vytvoř proměnnou adresy a ulož do proměnné list:
# adresy = [
   # "matous@holinka.com",
   # "danek11@seznam.cz",
   # "rennud15@gmail.com",
   # "pepa@centrum.cz"
# ]
# vytvoř funkci filtruj_adresy_s_cisly, funkce bude mít jeden parameter, posbírá ze zadaného setu pouze emaily, které obsahují čísla,
# výstup z fuknce ulož do proměnné vysledek,
# vypiš obsah proměnné vysledek.
# Ukázka průběhu
# ['danek11@seznam.cz', 'rennud15@gmail.com']

adresy = [
   "matous@holinka.com",
   "danek11@seznam.cz",
   "rennud15@gmail.com",
   "pepa@centrum.cz"
]

def filtruj_adresy_s_cisly(seznam) -> list:
    vystup = []
    for adresa in seznam:
        for pismeno in adresa:
            if pismeno.isdigit():               # Milan: Je zbytečné sem dávat: is True
                vystup.append(adresa)               # Milan: Je zbytečné sem dávat: else: continue
                break
    return vystup

vysledek = filtruj_adresy_s_cisly(adresy)
print(vysledek)

# Jiné řešení:
# Vytvor list se zadanymi hodnotami
adresy = [
    "matous@holinka.com",
    "danek11@seznam.cz",
    "rennud15@gmail.com",
    "pepa@centrum.cz"
]
def filtruj_adresy_s_cisly(emaily: list) -> list:
    """
    Ze zadaneho objektu emailu vyber pouze ty, ktere obsahuji ciselne znaky.
    Priklad:
    print(filtruj_adresy_s_cisly(["matous@holinka.com", "danek11@seznam.cz"]))
    ["danek11@seznam.cz"]
    """
    ciselne_hodnoty = []
    for email in emaily:
        for znak in email:
            if not znak.isnumeric():
                continue
            ciselne_hodnoty.append(email)
            break
    return ciselne_hodnoty
# Uloz vystup funkce do promenne
vysledek = filtruj_adresy_s_cisly(adresy)
# Vytiskni obsah promenne vysledek
print(vysledek)
