#  této úloze vytvoř program, který ukládá slova, která mají délku čtyři znaky. Jakmile uloží tři taková slova, skončí.
# Jednotlivé kroky, které program musí obsahovat:
# Definuj novou proměnnou slova, kam budeš slova ukládat,
# zapiš proces, který ukládá vstupy uživatele do proměnné slovo,
# tento proces pracuje tak dlouho, dokud proměnná slova neobsahuje tři unikátní slova,
# pokud je uživatelem vybrané slovo již součástí objektu slova, potom vypiš zprávu "Slovo <slovo> už je uložené",
# pokud není uživatelem vybrané slovo dlouhé čtyři znaky, vypiš zprávu "Slovo není dlouhé čtyři znaky",
# pokud je uživatelem vybrané slovo dlouhé čtyři znaky, potom jej přidej do proměnné slova,
# jakmile proces skončí (proměnná slova obsahuje tři hodnoty), vypiš zprávu "Už mám uložené tři slova".
# Ukázka průběhu:
# ZADEJ SLOVO ZE ČTYŘ:auto
# ZADEJ SLOVO ZE ČTYŘ:bota
# ZADEJ SLOVO ZE ČTYŘ:test
# Už mám uložené tři slova
# Pokud uživatel nezadá čtyři znaky dlouhé slovo:
# ZADEJ SLOVO: zidle
# Slovo není dlouhé čtyři znaky
# ZADEJ SLOVO:
# ...
# Pokud uživatel zadá slovo, které je již uložené:
# ZADEJ SLOVO ZE ČTYŘ:auto
# ZADEJ SLOVO ZE ČTYŘ:auto
# Slovo auto už je uložené
# ZADEJ SLOVO ZE ČTYŘ:
# ...

slova = set()
while len(slova) < 3:
    slovo = input('Zadej slovo:')           # str(input...)? je input vždy str? Nebo např. int?
    if slovo in slova:
        print(f'Slovo {slovo} už je uložené.')
        continue                            # continue je asi zbytečné
    elif len(slovo) != 4:
        print("Slovo není dlouhé čtyři znaky.")
        continue                            # continue je asi zbytečné
    else:
        slova.add(slovo)
else:
    print('Už mám uložené tři slova.')
