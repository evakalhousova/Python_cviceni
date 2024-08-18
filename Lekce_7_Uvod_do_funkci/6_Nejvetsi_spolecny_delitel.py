# NSD (GCD v angličtině) je zkratka pro největší společný dělitel (greatest common divisor).
# Tvým úkolem je vytvořit funkci najdi_gcd, která spočítá největší společný dělitel dvou celých čísel (int).
# Zadaná čísla jsou 12 a 16.
# Pomůcka, jak spočítat největší společný dělitel:
# hledáš největší společný dělitel pro čísla 12 a 16,
# nejprve použiješ modulo, abys zjistil zbytek 12 % 16, tedy 12,
# nyní vezmeš jako první číslo 16, tedy 16 % 12, kdy 12 představuje zbytek po prvním dělení. Zbytek po dělení 4,
# třetí krok se v podstatě opakuje, vezmu předchozí druhou hodnotu a zbytek po dělení, tedy 12 % 4, nyní je však zbytek 0, takže hledání je u konce,
# největší společný dělitel pro čísla 12 a 16 je 4.
# Jednotlivé kroky, které program musí obsahovat:
# Ulož zadaná čísla do proměnných:
# prvni_cislo = 12
# druhe_cislo = 16
# vytvoř uživatelskou funkci najdi_gcd s parametry x1, x2,
# najdi největšího společného dělitele a ulož jej do proměnné vysledek,
# vypiš obsah proměnné vysledek.
# Ukázka průběhu
# 4

prvni_cislo = 12
druhe_cislo = 16

def najdi_gcd (x1, x2):
    if x1 % x2 !=0:         # 12/16 = 0, zbytek 12, takže x1 % x2 = 12
        if x2 % (x1 % x2) !=0:          # 16/12 = 1, zbytek 4, takže x2 % (x1 % x2) = 4
            if (x1 % x2) % (x2 % (x1 % x2)) == 0:            # 12/4 = 3, zbytek 0,
                gcd = x2 % (x1 % x2)
        else:
            gcd = x1 % x2
    else:
        gcd = x2
    return gcd

vysledek = najdi_gcd(prvni_cislo, druhe_cislo)
print(vysledek)


# Jiné řešení:
# Vytvoř proměnné a ulož do nich zadaná čísla
prvni_cislo = 12
druhe_cislo = 16
def najdi_gcd(x1: int, x2: int) -> int:
    """
    Vrať celočíselnou hodnotu představující největší společný dělitel pro
    parametry "x1" a "x2".
    """
    while x2 > 1:
        zbytek_po_deleni = x1 % x2
        if not zbytek_po_deleni:
            break
        x1, x2 = x2, zbytek_po_deleni
    return x2
# Najdi největšího společného dělitele a ulož jej do proměnné
vysledek = najdi_gcd(prvni_cislo, druhe_cislo)
# Tisk výsledku
print(vysledek)
