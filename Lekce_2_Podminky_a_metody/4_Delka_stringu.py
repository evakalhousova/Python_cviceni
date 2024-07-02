# Zapiš tyto vstupní proměnné: zadana_slova = ["Matous", "Martin", "ahoj","er", "es", "i", "a"]
# pomocí indexu vyber libovolnou hodnotu z listu zadana_slova,
# zjisti délku vybraného slova a ulož tuto hodnotu do proměnné delka_slova,
# pokud je délka slova větší než 4 nebo rovná, vypíše větu '<slovo> počet znaků: <delka_slova>',
# pokud je délka slova menší než 3 a větší než 1, vypíše '<slovo> počet znaků: 2',
# pokud je délka slova rovná 1, vypíše '<slovo> počet znaků 1'.

zadana_slova = ["Matous", "Martin", "ahoj","er", "es", "i", "a"]
slovo = zadana_slova[5]
delka_slova = len(slovo)
if delka_slova >= 4:
    print(slovo, 'počet znaků:', delka_slova)
elif delka_slova > 1:
    print(slovo, 'počet znaků:', 2)
else:
    print(slovo, 'počet znaků:', 1)


# Řešení - jiné než moje:

# Zadaná slova
zadana_slova = ["Matous", "Martin", "ahoj", "er", "es", "i", "a"]
# Uživatel vybere pomocí indexu libovolný string z listu 'zadana_slova'
slovo = zadana_slova[0]
# Zjistí délku slova a uloží ji do proměnné 'delka_slova'
delka_slova = len(slovo)
# Pokud je hodnota v proměnné 'delka_slova' větší než nebo rovna 4
if delka_slova >= 4:
    print(slovo,  "počet znaků:", delka_slova)
# ..pokud je hodnota v proměnné 'delka_slova' větší než 1 a menší než 3
elif 3 > delka_slova > 1:
    print(slovo, "počet znaků: 2")
# ..pokud je hodnota v proměnné 'delka_slova' přesně 1 znak
elif delka_slova == 1:
    print(slovo,  "počet znaků: 1")