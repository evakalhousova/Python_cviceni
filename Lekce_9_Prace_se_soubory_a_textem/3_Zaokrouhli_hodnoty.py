# Zkus si trochu pohrát s formátováním stringů a s přesností.
# Program bude obsahovat tyto kroky:
# Na začátek souboru zapiš tyto proměnné:
# kombinace = 1.234
# presnost_str = "Hello"
# presnost_cisla = 123.4567
# použij proměnnou formatovana_presnost, kam naformátuješ hodnotu v presnost_cisla tak, aby výstup vypadal: |1.23e+02|123.5|123.46|,
# dále zapiš proměnnou formatovana_kombinace, kam naformátuješ hodnotu v kombinace, aby výstup vypadal: |1.234$|,
# nakonec zapiš proměnnou formatovana_presnost_str, kam naformátuješ hodnotu v presnost_str, aby výstup vypadal: |Hell|,
# v neposlední řadě vypiš pomocí funkce print výstup podle vzoru níže a jednotlivé hodnoty zarovnej pomocí tabulátorů,
# obsah proměnných pod sebe zapiš do textového souboru vysledek.txt.
# Ukázka průběhu
# Naformátovaná přesnost:         |1.23e+02|123.5|123.46|,
# Naformátovaná kombinace:        |1.234$|,
# Naformátovaný string:           |Hell|.
# Zapisuji do souboru
# Textový soubor vysledek.txt potom bude obsahovat:
# |1.23e+02|123.5|123.46|
# |1.234$|
# |Hell|

kombinace = 1.234
presnost_str = "Hello"
presnost_cisla = 123.4567

formatovana_presnost = f'|{presnost_cisla:.3}|{presnost_cisla:.4}|{presnost_cisla:.5}|'
formatovana_kombinace = f'|{kombinace:$<6}|'
formatovana_presnost_str = f'|{presnost_str[0:4]}|'

vystup = f'''Naformátovaná přesnost:          {formatovana_presnost},
Naformátovaná kombinace:         {formatovana_kombinace},
Naformátovaný string:            {formatovana_presnost_str}.'''

print(f'''{vystup}
Zapisuji do souboru''')             # Taky jsem mohla použít sep='\n'

cesta = 'C:/Python/Projekt_1/Lekce_9_Prace_se_soubory_a_textem/vysledek.txt'
with open(cesta, mode='w', encoding='utf-8') as f:
    f.write(formatovana_presnost + '\n' + formatovana_kombinace + '\n' + formatovana_presnost_str)


#Jiné řešení (Engeto):

# Vstupní proměnné
kombinace = 1.234
presnost_str = "Hello"
presnost_cisla = 123.4567
# Přesnost pro číselné znaky
formatovana_presnost = \
    f"|{presnost_cisla:.3}|{presnost_cisla:.4}|{presnost_cisla:.5}|"
# Přesnost a ostatní specifikátory
formatovana_kombinace = f"|{kombinace:$<6.4}|"
# Přesnost u stringu
formatovana_presnost_str = f"|{presnost_str:.4}|"
# Výpis hodnot
print(f"""\
Naformátovaná přesnost: \t{formatovana_presnost},
Naformátovaná kombinace: \t{formatovana_kombinace},
Naformátovaný string: \t\t{formatovana_presnost_str}.""")
# Ulož proměnné do souboru 'vysledek.txt'
print("Zapisuji do souboru")
with open("vysledek.txt", mode="w") as txt:
    txt.write("\n".join(
        (formatovana_presnost, formatovana_kombinace, formatovana_presnost_str)
        )
    )
