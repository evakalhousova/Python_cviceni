# V této úloze vytvoř program, který vytiskne, kolikrát se každý objekt nachází v daném listu, tuplu, nebo stringu (u stringu chceme počet jednotlivých znaků).
# Jednotlivé kroky, které program musí obsahovat:
# Vytvoř list se jménem sequence, který obsahuje hodnoty: [1, 21, 5, 3, 5, 8, 321, 1, 2, 2, 32, 6, 9, 1, 4, 6, 3, 1, 2],
# vytvoř prázdný dict se jménem counts,
# iteruj skrze zadanou sekvenci hodnot sequence,
# pokud vybrané číslo není ve vytvořeném slovníku, přidej jej a nastav mu hodnotu 1,
# pokud vybrané číslo je ve vytvořeném slovníku, inkrementuj jeho hodnotu,
# nakonec nasbírané klíče setřid a vypiš na každý řádek nejprve číslo a následně jeho výskyt key: <cislo>, value: <vyskyt>.

sequence = [1, 21, 5, 3, 5, 8, 321, 1, 2, 2, 32, 6, 9, 1, 4, 6, 3, 1, 2]
counts = {}
for cislo in sequence:
    if cislo not in counts:
        counts[cislo] = 1
    else:
        counts[cislo] = counts.get(cislo) + 1
sorted_keys = list(counts)
sorted_keys.sort()
for cislo in sorted_keys:
    print('key:', cislo, 'value:', counts.get(cislo))


# Jiné řešení:

# Zadané hodnoty
sequence = [1, 21, 5, 3, 5, 8, 321, 1, 2, 2, 32, 6, 9, 1, 4, 6, 3, 1, 2]
counts = {}
# Cyklus, který spočítá jednotlivé výskyty čísel
for number in sequence:

    # .. pokud číslo není uložené, eviduj jej jako první hodnotu
    if number not in counts:
        counts[number] = 1

    # .. pokud číslo je uložené, inkrementuj původní hodnotu
    else:
        counts[number] = counts[number] + 1
# Setřiď podle klíče a vypiš seřazené hodnoty
for key, value in sorted(counts.items()):
    print("key:", key, "value:", value)
