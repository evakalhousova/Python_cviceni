# Viz cvičení 7_Skript_na_serazeni.py
# Použití funkce sorted a metody sort:

jmena = [
    'Michal', 'Pepa', 'Honza',
    'Pavel', 'Lukas', 'Matej',
    'Iva', 'Klara', 'Jana',
    'Honza', 'Vasek','Milan',
    'Michal'
]

# Funkce sorted je jednodušší řešení:
print(sorted(jmena))

# Metoda sort list sice seřadí, ale vrací hodnotu "None", takže se print musí udělat jako druhá akce:
# None:
print(jmena.sort())
# Print seřazeného listu:
jmena.sort()
print(jmena)
