# V této úloze vytvoř program, který potřebuje od uživatele start, stop a delitel.
# Po zapracování vypíše všechna celá čísla v intervalu od start, do stop, která jsou dělitelná hodnotou v delitel.
# Jednotlivé kroky, které program musí obsahovat:
# Vytvoř tyto proměnné:
# vysledek = list()
# start = 3
# stop = 9
# delitel = 3
# ověří jestli jsou proměnné start, stop a delitel datový typ int (pomocí built-in funkce isinstance),
# pokud jsou int, vypiš oznámení dle ukázky níž,
# pokud alespoň jeden není int, vypiš oznámení dle ukázky níž a ukonči skript,
# jestli jsou jednotlivé hodnoty z intervalu dělitelné hodnotou v proměnné delitel, potom je přidej do zadaného seznamu vysledek,
# po skončení iterace všech hodnot vypiš výsledné hodnoty podle vzoru níže.
#Ukázka průběhu:
# Start: 3, Stop: 9, Dělitel: 3
# Zadaný rozsah: <3, 9>
# Čísla dělitelná 3: [3, 6, 9]
# Pokud uživatel nezadá číselné hodnoty:
# Start: 3, Stop: 9, Dělitel: "a"
# Zadané vstupy musí být čísla.

vysledek = list()
start = 3
stop = 9
delitel = 3
if isinstance(start, int) == True and isinstance(stop, int) == True and isinstance(delitel, int) == True:
    for cislo in range(start, stop + 1):
        if cislo % delitel == 0:
            vysledek.append(cislo)
    print(f'# Start: {start}, Stop: {stop}, Dělitel: {delitel}')
    print('Zadaný rozsah: <', start, ',', stop, '>')
    print('Čísla dělitelná 3:', vysledek)
else:
    print(f'# Start: {start}, Stop: {stop}, Dělitel: "{delitel}"')
    print('Zadané vstupy musí být čísla.')


# Jiné řešení:

# Zadaná proměnná
vysledek = []
# Zadané hodnoty: počáteční hodn., konečná hodn., dělitel
start = 3
stop = 9
delitel = 3
if isinstance(start, int) \
        and isinstance(stop, int) \
        and isinstance(delitel, int):
    print("Zadaný rozsah: <", start, ", ", stop, ">", sep="")           # Otázka: sep="" zaručí, aby tam nebyly redundantní mezery?
    # Iteruj skrze rozsah zadaných čísel
    for number in range(start, stop + 1):
        # .. pokud je vybrané číslo dělitelné hodnotou v prom. "delitel"
        if number % int(delitel) == 0:
            # .. přidej jej do seznamu "vysledek"
            vysledek.append(number)
    # doplň výpis hodnot v proměnné 'vysledek'
    print('Čísla dělitelná', delitel, ':', vysledek)
else:
    print("Zadané vstupy musí být čísla.")
