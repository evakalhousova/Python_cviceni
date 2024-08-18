# Převaděč bude umět následující:
# Převod z kilogramů na libry,
# z kilometrů na míle,
# z litrů na galony.
# Na začátek máš předepsané převodní poměry k jednotkám:
# kg_lb = 2.20
# km_mile = 0.62
# l_gal = 0.26
# dále vytvoř proměnné s počtem jednotek kg_pocet , km_pocet, l_pocet:
# kg_pocet = 80
# km_pocet = 54
# l_pocet = 5
# poté proměnné s výpočtem kg_vysledek, km_vysledek , l_vysledek,
# nakonec výsledky přehledně vypiš.

kg_lb = 2.20
km_mile = 0.62
l_gal = 0.26
kg_pocet = 80
km_pocet = 54
l_pocet = 5
kg_vysledek = kg_pocet * kg_lb
km_vysledek = km_pocet * km_mile
l_vysledek = l_pocet * l_gal
print(kg_pocet, 'kg je', kg_vysledek, 'lb')
print(km_pocet, 'km je', km_vysledek, 'mil')
print(l_pocet, 'l je', l_vysledek, 'gal')
