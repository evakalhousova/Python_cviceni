# Tvým úkolem bude ověřit správnost prvního písmene každého dne v týdnu. Postup bude vypadat následovně:
# Zapiš tyto vstupní proměnné:
# vstupni_cisla = [1, 2, 3, 4, 5, 6, 7]
# vstupni_pismena = ["p", "ú", "s", "č", "p", "s", "n"]
# tyden = ('pondělí', 'úterý', 'středa', 'čtvrtek', 'pátek', 'sobota', 'neděle')
# vytvoř proměnnou cislo_dne a zapiš do ní hodnotu 3,
# ověř, jestli hodnota v cislo_dne je v listu vstupni_cisla,
# pokud není, vypiš výstup podle vzoru níže,
# pokud je, vypiš zprávu "Správná vstupní hodnota!"
# .. dále vytvoř proměnnou den_tydne a pomocí upravené hodnoty v proměnné cislo_dne, naindexuj z proměnné tyden požadovaný den (př. 1 --> "pondělí", 2 --> "úterý"),
# ověř, jestli vybraný str v proměnné den_tydne má stejné počáteční písmeno, jako jsou v proměnné vstupni_pismena (ověř opět pomocí upraveného indexu),
# .. pokud se znaky shodují vypiš "Správné písmeno",
# .. pokud se znaky neshodují vypiš "Špatné písmeno".

vstupni_cisla = [1, 2, 3, 4, 5, 6, 7]
vstupni_pismena = ["p", "ú", "s", "č", "p", "s", "n"]
tyden = ('pondělí', 'úterý', 'středa', 'čtvrtek', 'pátek', 'sobota', 'neděle')
cislo_dne = 9
if cislo_dne in vstupni_cisla:
    print('Správná vstupní hodnota!')
    den_tydne = tyden[cislo_dne -1]
    if den_tydne[0] == vstupni_pismena[cislo_dne -1]:   # jiné řešení: if den_tydne.startswith(vstupni_pismena[cislo_dne - 1]):
        print('Správné písmeno')
    else:
        print('Špatné písmeno')
else:
    print('Špatná vstupní hodnota!')


