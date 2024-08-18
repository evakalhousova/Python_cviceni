# Pomocí modulu os napiš takový kód, který v aktuálním umístění vytvoří tyto tři prázdné adresáře:
# obrazky,
# texty,
# gify.
# Program musí:
# Nahrát knihovnu os,
# vytvořit proměnnou jmena_slozek, kam vložíš stringy "obrazky", "texty", "gify",
# projít jednu hodnotu za druhou z proměnné jmena_slozek,
# ověřit, jestli daný string neexistuje a není adresářem,
# pokud existuje, vypsat oznámení "Složka již existuje!"
# pokud neexistuje, vytvořit složku a vypsat oznámení "Tvořím novou složku: <jmeno>".
# závěrem vypsat: "Všechny složky existují".


import os
jmena_slozek = ['obrazky', 'texty', 'gify']
for jmeno in jmena_slozek:
    path = f'C:/Python/Projekt_1/Lekce_6_Knihovny_moduly_a_balicky/{jmeno}'
    if os.path.exists(path) is True:            # Milan: is True tady být vůbec nemusí. Engeto - jiné řešení: if os.path.exists(jmeno) and os.path.isdir(jmeno):
        print('Složka již existuje!')
    else:
        os.mkdir(path)
        print(f'Tvořím novou složku: {jmeno}')
print('Všechny složky existují.')
