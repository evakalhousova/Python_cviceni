# V této úloze vytvoř program, který seřadí abecedně zadaný seznam jmena.
# poznámka. bez použití funkce sorted nebo metody seznamů sort .
# Jednotlivé kroky, které program musí obsahovat:
# Vytvoř proměnnou jmena, která je dat. typ list a obsahuje:
# jmena = [
# 'Michal', 'Pepa', 'Honza',
# 'Pavel', 'Lukas', 'Matej',
# 'Iva', 'Klara', 'Jana',
# 'Honza', 'Vasek','Milan',
# 'Michal'
# ]
# vytvoř kopii proměnné jmena, do proměnné kopie_jmen,
# iteruj přes zadaný seznam jmena,
# vytvoř vnitřní (nestovanou) smyčku, která bude sledovat hodnotu indexu o jedna vyšší než aktuální hodota indexu z první smyčky,
# pokud je hodnota v listu na indexu z první smyčky vyšší než hodnota na indexu druhé smyčky, aktualizuj pořadí hodnot v listu,
# vypiš seřazenou podobu seznamu jmena.

# Řešení - Engeto:          # Na tohle jsem sama nepřišla, nevěděla jsem, že jdou srovnávat hodnoty stringů: kopie_jmen[i] > kopie_jmen[j]: viz https://docs.python.org/3/tutorial/datastructures.html#comparing-sequences-and-other-types

# Zadané proměnné
jmena = [
    'Michal', 'Pepa', 'Honza',
    'Pavel', 'Lukas', 'Matej',
    'Iva', 'Klara', 'Jana',
    'Honza', 'Vasek','Milan',
    'Michal'
]
kopie_jmen = jmena.copy()
# Iterace k získání indexů v listu "jmena"
for i in range(len(kopie_jmen)):
    # Iterace k získání indexu, který je o 1 vyšší než aktuální hodnota i
    for j in range(i + 1, len(kopie_jmen)):
        # Pokud je hodnota na indexu i větší než hodnota na indexu j aktualizuj
        # ..pořadí hodnot v listu za pomocí indexů
        if kopie_jmen[i] > kopie_jmen[j]:
            kopie_jmen[i], kopie_jmen[j] = kopie_jmen[j], kopie_jmen[i]
# Vypiš výsledek
print(kopie_jmen)
