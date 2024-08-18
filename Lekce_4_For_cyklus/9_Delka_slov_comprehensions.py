# Pomocí slovníkové komprehence spočítej délky slov v zadané sekvenci.
# Skript bude obsahovat:
# Zadanou proměnnou seznam_slov, s hodnotami: ["jablko", "pomeranč", "banán", "kiwi", "hruška"],
# do proměnné delky_slov zapiš slovníkovou komprehenci tak, aby ukládála hodnoty ve formátu:slovo: delka_slova, tedy:"svetr": 5,
# nakonec vypiš výsledek pomocí funkce print.
# Ukáza průběhu:
# {'jablko': 6, 'pomeranč': 8, 'banán': 5, 'kiwi': 4, 'hruška': 6}

seznam_slov = ["jablko", "pomeranč", "banán", "kiwi", "hruška"]
delky_slov = {slovo: len(slovo) for slovo in seznam_slov}
print(delky_slov)
