# Tentokrát bude tvým úkolem napsat dvě funkce:
# je_prvocislo, která posoudí, jestli je zadané číslo prvočíslo, nebo není,
# generuj_interval_prvocisel, která vytvoří interval prvočísel až po zadanou hodnotu.
# Prvočísla jsou taková čísla, která jsou dělitelná pouze jedničkou nebo sama sebou.
# Tvoje úloha musí obsahovat tyto kroky:
# Vytvoř funkci je_prvocislo, s parametrem cislo, který vezme samotné číslo a jako druhý parametr prvocisla,
# vytvoř funkci generuj_interval_prvocisel, která nejprve vytvoří interval všech čísel od nuly až po parametr stop (včetně této hodnoty),
# prochází interval a všechny jeho hodnoty. Pokud narazí na 0 nebo 1, přeskoč je,
# vytvoř zanořený cyklus, který prochází hodnoty v rozsahu range(2, cislo),
# pokud platí, že hodnota z vnějšího cyklu cislo je dělitelná beze zbytku hodnotou z vnitřního cyklu filtr_cislo, přeruš vnitřní cyklus. Nakonec ulož hodnotu v filtr_cislo do proměnné vysledek,
# získané údaje vrať jako tuple,
# vyzkoušej tvoji úlohu na těchto voláních:
# je_prvocislo(23, generuj_interval_prvocisel(30)),
# je_prvocislo(233, generuj_interval_prvocisel(300)),
# je_prvocislo(146, generuj_interval_prvocisel(300)),
# Ukázka výstupu
# True
# True
# False

# Nemám to hotové:

def je_prvocislo(cislo, prvocisla):
    return bool(cislo in prvocisla)                 # To bool tam být nemusí.

def generuj_interval_prvocisel(stop):
    vysledek = []
    for hodnota in range(stop):
        if hodnota == 0 or hodnota == 1:
            continue
        for filtr_cislo in range(2, hodnota):           # Ten range musí být omezen tou hodnotou, aby se to nedělilo samo sebou.
            if hodnota % filtr_cislo == 0:
                break
        else:
            vysledek.append(hodnota)
    return tuple(vysledek)

print(je_prvocislo(23, generuj_interval_prvocisel(30)))
print(je_prvocislo(233, generuj_interval_prvocisel(300)))
print(je_prvocislo(146, generuj_interval_prvocisel(300)))
