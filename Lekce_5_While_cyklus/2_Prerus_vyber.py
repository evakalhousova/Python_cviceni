# V této úloze vytvoř program, který uživateli umožní vybrat ze zadaných hodnot. Pokud zapíše cokoliv jiného, program jej upozorní a nechá jej vybírat tak dlouho, dokud nezadá validní hodnotu.
# Jednotlivé kroky, které program musí obsahovat:
# Definovat objekt ovoce, který obsahuje unikátní stringy "jablko", "banan", "citron", "pomeranc",
# vypsat uživateli všechno uložené ovoce v proměnné ovoce spojené znaky ", ",
# vybrat si ovoce z nabídky pomocí funkce input do proměnné vyber s ohlášením "VYBER Z DOSTUPNÉHO OVOCE:",
# pokud si uživatel nevybere z nabídky, vypsat: "Ovoce není v nabídce." a nechat jej vybírat tak dlouho, pokud nezadá jeden ze stringů v proměnné ovoce,
# pokud si uživatel vybere jednu z možností v ovoce, potom program vypíše "Bezva, toto ovoce je v nabídce.".
# Ukázka průběhu:
# Dostupné ovoce: citron, banan, pomeranc, jablko
# VYBER Z DOSTUPNÉHO OVOCE:citron
# Bezva, toto ovoce je v nabídce
# Pokud uživatel nevybere zadané ovoce:
# Dostupné ovoce: jablko, pomeranc, citron, banan
# VYBER Z DOSTUPNÉHO OVOCE:svestka
# Ovoce není v nabídce
# VYBER Z DOSTUPNÉHO OVOCE:

ovoce = {'jablko', 'banan', 'citron', 'pomeranc'}
print("Dostupné ovoce:", ", ".join(ovoce))
print('Dostupné ovoce:', ovoce, sep=", ")           # Chyba, ve výstupu jsou symboly navíc, vypadá to ošklivě! Správné řešení: print("Dostupné ovoce:", ", ".join(ovoce))
while (vyber := input('VYBER Z DOSTUPNÉHO OVOCE:')) not in ovoce:
    print('Ovoce není v nabídce.')
    continue
else:
    print('Bezva, toto ovoce je v nabídce.')


# Jiné řešení:

# Zadaný objekt s jednotlivými hodnotami
ovoce = {"jablko", "banan", "citron", "pomeranc"}
# Vypsat všechny hodnoty v proměnné 'ovoce'
print("Dostupné ovoce:", ", ".join(ovoce))
# Vyběr ovoce ponechat možný tak dlouho, dokud uživatel nezadá hodnotu z 'ovoce'
while True:
    # Výběr ulož do proměnné 'vyber'
    vyber = input("Vyber z dostupného ovoce: ".upper())
    # pokud uživatel vybere jinou hodnotu, než jsou v 'ovoce', proces zopakuj
    if vyber not in ovoce:
        print("Ovoce není v nabídce.")
    # pokud uživatel vybere hodnoty z proměnné `ovoce`, proces přeruš
    else:
        print("Bezva, toto ovoce je v nabídce.")
        break                                                        # Otázka: Je tady zapotřebí break?
