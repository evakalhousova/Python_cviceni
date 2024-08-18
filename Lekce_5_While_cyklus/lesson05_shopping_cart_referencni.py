#!/usr/bin/python3.8

kosik = {}
ODDELOVAC = "=" * 40
POTRAVINY = {
    "mleko": [30, 5],  # index '0'-> cena, index '1' -> pocet
    "maso": [100, 1],
    "banan": [30, 10],
    "jogurt": [10, 5],
    "chleb": [20, 5],
    "jablko": [10, 10],
    "pomeranc": [15, 10],
}

print("Vitejte u naseho nakupniho kosiku!".center(len(ODDELOVAC)), ODDELOVAC, sep="\n")

for potravina in POTRAVINY:
    print(
        f"| POTRAVINA: {potravina: ^9}| CENA: {POTRAVINY[potravina][1]: ^3} |".center(
            len(ODDELOVAC)
        )
    )
else:
    print(ODDELOVAC)

while (zbozi := input("Zbozi:")) != "q":
    if zbozi not in POTRAVINY:
        print(f"Zbozi '{zbozi}' neni v nabidce")

    elif zbozi not in kosik and POTRAVINY[zbozi][1] > 0:
        kosik[zbozi] = [POTRAVINY[zbozi][0], 1]
        POTRAVINY[zbozi][1] = POTRAVINY[zbozi][1] - 1

    elif zbozi in kosik and POTRAVINY[zbozi][1] > 0:
        kosik[zbozi][1] = kosik[zbozi][1] + 1
        POTRAVINY[zbozi][1] = POTRAVINY[zbozi][1] - 1

    elif POTRAVINY[zbozi][1] == 0:
        print(f"Zbozi '{zbozi}' neni skladem")

else:
    print(ODDELOVAC)
    celkem = 0

    for zbozi, cisla in kosik.items():
        cena = cisla[0]
        pocet = cisla[1]
        celkem = celkem + (mezisoucet := cena * pocet)
        print(
            f"{zbozi: ^8}:{cena:>4} x {pocet:<2}= {mezisoucet:>3},-".center(
                len(ODDELOVAC)
            )
        )

    else:
        print(ODDELOVAC)
        if (odpoved := input("Pokracovat k platbe (y/n):")) == "y":
            print(
                ODDELOVAC,
                f"Prechazim k platbe {celkem},-..".center(len(ODDELOVAC)),
                sep="\n",
            )
        elif odpoved == "n":
            print(ODDELOVAC, "Ukoncuji nakup..".center(len(ODDELOVAC)), sep="\n")
        else:
            print(
                ODDELOVAC,
                "Neplatna operace, ukoncuji nakup..".center(len(ODDELOVAC)),
                sep="\n",
            )
