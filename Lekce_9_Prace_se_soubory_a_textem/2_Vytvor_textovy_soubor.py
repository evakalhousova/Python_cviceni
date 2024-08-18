# V této úloze si procvičíš zapisování a čtení obsahu textového souboru.
# Tvůj zápis musí obsahovat následující:
# Nejdřív zapiš pomocné proměnné:
# prvni_radek = "První řádek v souboru,\n"
# druhy_radek = "druhý řádek v souboru,\n"
# treti_radek = "třetí řádek v souboru."
# následně zapiš zadané proměnné do nového souboru txt_soubor.txt a ulož jej do objektu txt_soubor,
# dále zapiš postupně (nebo zaráz) všechny tři zadané proměnné prvni_radek, druhy_radek a treti_radek,
# po zapsání soubor zavři,
# znovu soubor otevři a tentokrát přečti a ulož jeho obsah do proměnné obsah_txt,
# nakonec vypiš obsah proměnné obsah_txt pomocí funkce print.

prvni_radek = "První řádek v souboru,\n"
druhy_radek = "druhý řádek v souboru,\n"
treti_radek = "třetí řádek v souboru."

cesta = 'C:/Python/Projekt_1/Lekce_9_Prace_se_soubory_a_textem/txt_soubor.txt'
with open(cesta, mode='w', encoding='utf-8') as txt_soubor:
    txt_soubor.write(prvni_radek + druhy_radek + treti_radek)           # Zapsání tří řádků zaráz pomocí symbolu +

# Zapsání tří řádků postupně:
# txt_soubor.write(prvni_radek)
# txt_soubor.write(druhy_radek)
# txt_soubor.write(treti_radek)

with open(cesta, mode="r", encoding='utf-8') as f:
    obsah_txt = f.readlines()

print(obsah_txt)


# Jiné řešení (Engeto):

# zapiš pomocné proměnné
prvni_radek = "První řádek v souboru,\n"
druhy_radek = "druhý řádek v souboru,\n"
treti_radek = "třetí řádek v souboru."
# zapiš proměnné do nového txt souboru
txt_soubor = open("txt_soubor.txt", mode="w")
txt_soubor.write(prvni_radek)
txt_soubor.write(druhy_radek)
txt_soubor.write(treti_radek)
txt_soubor.close()
# přečti a ulož obsah txt souboru
cteni_txt = open("txt_soubor.txt")
obsah_txt = cteni_txt.readlines()
# vypiš výsledek
print(obsah_txt)
