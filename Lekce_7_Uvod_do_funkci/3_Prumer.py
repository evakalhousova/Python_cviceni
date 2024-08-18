# Vytvoř funkci, která spočítá průměrnou hodnotu pro danou sekvenci číselných hodnot.
# Jednotlivé kroky, které program musí obsahovat:
# Vytvoř proměnnou sekvence_cisel:
# sekvence_cisel = [35, 14, 26, 48, 49, 26, 18, 25, 16, 16, 39, 17, 10, 29, 30]
# vytvoř funkci spocitej_prumer, která spočítá průměr zadaných hodnot,
# zadej funkci nachystaný seznam čísel a ulož výsledek do proměnné vysledek,
# vypiš výsledek.
# Ukázka průběhu
# 26.533333333333335

sekvence_cisel = [35, 14, 26, 48, 49, 26, 18, 25, 16, 16, 39, 17, 10, 29, 30]

def spocitej_prumer(seznam):
    return sum(seznam) / len(seznam)

vysledek = spocitej_prumer(sekvence_cisel)
print(vysledek)
