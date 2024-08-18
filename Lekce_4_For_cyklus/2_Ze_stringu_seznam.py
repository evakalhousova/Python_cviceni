# V této úloze vytvoř program, který převede zadaný string na list.
# Jednotlivé kroky, které program musí obsahovat:
# Zapiš proměnnou vysledek, která obsahuje prázdný list,
# zapiš proměnnou zadana_cisla, která obsahuje datový typ str s hodnotou '1, 2, 3, 4, 5',
# rozděl hodnotu v proměnné zadana_cisla pomocí symbolu ,, výsledek ulož do proměnné cisla,
# postupně projdi hodnoty v proměnné cisla, očisti hodnoty a ulož je do proměnné vysledek,
# nakonec zobraz uložená čísla s doplňujícím textem: List:.

vysledek = []
zadana_cisla = '1, 2, 3, 4, 5'
cisla = zadana_cisla.split(',')                 #Moje řešení nefungovalo: cisla = zadana_cisla.split(', ')
for cislo in cisla:
    ocistene_cislo = int(cislo.strip())         #Moje řešení nefungovalo: int(cislo)
    vysledek.append(ocistene_cislo)             #Moje řešení nefungovalo: vysledek.append(cislo)
print('List:', vysledek)
