# ytvoř uživatelskou funkci, která zdvojnásobí všechny znaky zadaného stringu.
# Program musí obsahovat tyto kroky:
# Vytvoř proměnnou vstup:
# vstup = 'Ahoj všem'
# vytvoř funkci zdvojnasob_vsechny_znaky, která bude mít jeden parametr zadani,
# vytvoř proměnnou vysledek do které ulož výstup funkce,
# vypiš hodnotu proměnné vysledek.
# Ukázka průběhu
# AAhhoojj  vvššeemm

vstup = 'Ahoj všem'
def zdvojnasob_vsechny_znaky(zadani):
    s = ''
    for pismeno in zadani:
        s += pismeno * 2
    return s

vysledek = zdvojnasob_vsechny_znaky(vstup)
print(vysledek)


# Jiné řešení:
# Vytvor promennou a uloz zadanou hodnotu
vstup = "Ahoj všem"
# Vytvor funkci ktera vezme string na vstupu
def zdvojnasob_vsechny_znaky(zadani: str) -> str:
    zdvojene = []
    for znak in zadani:
        zdvojene.append(znak * 2)
    return "".join(zdvojene)
# Uloz vystup funkce do promenne vysledek
vysledek = zdvojnasob_vsechny_znaky(vstup)
# Vytiskni vysledek
print(vysledek)
