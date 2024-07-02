# V této úloze vytvoř program, který:
# Vytvoří proměnné:
# cisla_1 = (1, 1, 2, 3, 4)
# cisla_2 = (5, 6, 7, 7, 8)
# vytvoří ze zadaných proměnných sety,
# udělá sjednocení hodnot obou nově vzniklých setů a uloží jej do proměnné sjednocene_hodnoty,
# vypíše výsledek s ohlášením "Sjednocené hodnoty ze zadání:".

cisla_1 = (1, 1, 2, 3, 4)
cisla_2 = (5, 6, 7, 7, 8)
set_1 = set(cisla_1)
set_2 = set(cisla_2)
sjednocene_hodnoty = set_1.union(set_2)    # jiné řešení:  sjednocene_hodnoty = set_1 | set_2
print('Sjednocené hodnoty ze zadání:', sjednocene_hodnoty)


# Jiné řešení:

# Zadané tuply "cisla_1" a "cisla_2"
cisla_1 = (1, 1, 2, 3, 4)
cisla_2 = (5, 6, 7, 7, 8)
# Vytvoř sety a udělej sjednocení jejich hodnot
# ..do proměnné "sjednocene_hodnoty"
sjednocene_hodnoty = set(cisla_1) | set(cisla_2)
# Vypiš uložený výsledek v proměnné "sjednocene_hodnoty"
print("Sjednocené hodnoty ze zadání:", sjednocene_hodnoty)
