# V této úloze vytvoř program, který vypíše šachovnici (střídání černých '#' a bílých ' ' polí).
# Jednotlivé kroky, které program musí obsahovat:
# Vytvoř tyto vstupní proměnné:
# velikost = 10
# sachovnice = []
# symboly = ['#',' ']
# iteruj přes jednotlivé řádky šachovnice (velikost),
# v každém kroku iterace vytvoř proměnnou rada,
# následně iteruj přes jednotlivé buňky,
# vytvoř pomocnou proměnnou index, která vybere pomocí proměnné symbols aktuální pozici, (ať vytvoříš střídavě pole " " a "#"),
# postupně přidávej jednotlivé symboly do proměnné rada,
# na konci řádku přidej rada do proměnné sachovnice,
# na závěr spoj jednotlivé hodnoty v proměnné sachovnice pomocí \n a vypiš její obsah.

velikost = 10
sachovnice = []
symboly = ['#',' ']

for radek in range(velikost):
    rada = []
    if radek % 2 == 0:
        for bunka in range(velikost):               # Další iterace range(velikost)
            if bunka % 2 == 0:
                index = symboly[0]
            else:
                index = symboly[1]
            rada.append(index)
    else:
        for bunka in range(velikost):
            bunka = bunka + 1
            if bunka % 2 == 0:
                index = symboly[0]
            else:
                index = symboly[1]
            rada.append(index)
    sachovnice.append(rada)

for radek in sachovnice:
    print(''.join(radek))                           # Tady jsem na to nemohla přijít.


# Moje kratší řešení:

velikost = 10
sachovnice = []
symboly = ['#',' ']

for radek in range(velikost):
    rada = []
    if radek % 2 == 0:
        for bunka in range(velikost):               # Další iterace range(velikost)
            index = symboly[bunka % 2]
            rada.append(index)
    else:
        for bunka in range(velikost):
            bunka = bunka + 1
            index = symboly[bunka % 2]
            rada.append(index)
    sachovnice.append(rada)

for radek in sachovnice:
    print(''.join(radek))                           # Tady jsem na to nemohla přijít.


# Jiné řešení - Milan:
def sachovnice():
    size = 10
    symbols = ['⬛', '🟩']
    for row in range(size):
        for col in range(size):
            print(symbols[(row + col) % 2], end='')
        print()
sachovnice()


# Jiné řešení - Engeto:

velikost = 10
symboly = ['#',' ']
sachovnice = []
# Iteruj přes řádky šachovnice a vytvoř proměnnou "rada"
for radek in range(velikost):
    rada = []
    # Iteruj přes jednotlivé buňky v každém řádku
    for bunka in range(velikost):
        # Vytvoř index, který vybere jednu z hodnot v proměnné "symboly"
        index = (radek + bunka) % len(symboly)
        rada.append(symboly[index])
    # Přidej hotové buňky do proměnné "sachovnice"
    sachovnice.append(''.join(rada))
# Vypiš výslednou šachovnici
print('\n'.join(sachovnice))
