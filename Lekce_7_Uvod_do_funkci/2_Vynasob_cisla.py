# V této úloze napíšeš uživatelskou funkci, která vezme dvě číselné hodnoty a vrátí jejich součin.
# Program musí obsahovat tyto kroky:
# Vytvoř tyto dvě proměnné:
# prvni_cislo = 5
# druhe_cislo = 5
# vytvoř funkci vynasob, která bude mít 2 parametry num1 a num2,
# vytvoř proměnnou vysledek, do které ulož výstup funkce,
# vypiš hodnotu proměnné vysledek.
# Ukázka průběhu
# Vysledek je: 25

prvni_cislo = 5
druhe_cislo = 5

def vynasob(num1, num2):
    return num1 * num2

vysledek = vynasob(prvni_cislo, druhe_cislo)
print('Vysledek je: ', vysledek)            # Jiné řešení: print(f'Vysledek je: {vysledek}')
