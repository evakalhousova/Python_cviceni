kosik = {}
oddelovac = "=" * 40
# "=" * 3  --->   "==="

potraviny = {
    "mleko": [30, 5],  # index '0'-> cena, index '1' -> pocet
    "maso": [100, 1],
    "banan": [30, 10],
    "jogurt": [10, 5],
    "chleb": [20, 5],
    "jablko": [10, 10],
    "pomeranc": [15, 10],
}

print("Vitejte u naseho nakupniho kosiku!".center(len(oddelovac)), oddelovac, sep="\n")

for potravina, (cena, pocet) in potraviny.items():
    print(f"| POTRAVINA: {potravina: ^9} | CENA: {cena}")

# kosik = {potravina: [cena, pocet]}

while (zbozi := input("Vyber zbozi:")) not in {"q", "quit"}:
    if zbozi not in potraviny:
        print(f"Zbozi {zbozi} neni v nabidce")
    elif potraviny[zbozi][1] <= 0:
        print(f"Zbozi {zbozi} je vyprodano :(")
    elif zbozi not in kosik:
        kosik[zbozi] = [potraviny[zbozi][0], 1]
        potraviny[zbozi][1] -= 1
    else:
        kosik[zbozi][1] += 1
        potraviny[zbozi][1] -= 1
    print("Kosik: ", kosik)
    print("Potraviny: ", potraviny)


# Vypsat pro kazdy produkt mezisoucet a pak celkovou sumu nakupu
# Dat moznost uzivateli pokracovat v nakupu a nebo prejit do platby
# Vypsat uzivateli siimulaci platby (muzete si s tim pripadne pohrat i vic :-D )
# Ukoncit nakup a predat stvrzenku
