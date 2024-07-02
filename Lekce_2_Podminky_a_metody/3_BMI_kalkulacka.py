# Obecně je BMI (Body Mass Index) míra, která vyčísluje obezitu u lidí.
# Rovnice výpočtu BMI: váha / výška2
# Váha se udává v kilogramech a výška v metrech. Hodnoty, které z tohoto vzorečku dostaneme, škálujeme podle této tabulky:
# Hodnota	Význam
# < 18,5	Podvýživa
# 18,5 – 25	Zdravá váha
# 25 – 30	Mírná nadváha
# 30 – 40	Obezita
# 40 <	Těžká obezita
# V této úloze vytvoř program, který získá BMI uživatele Martin, který měří 200 centimerů a váží 80 kilogramů:
# Vytvoř proměnné jmeno, vaha, vyska a zadej do nich hodnoty,
# vytvoř proměnnou bmi a přiřaď k ní vzorec, pomocí proměnných vaha, vyska a aritmetického operátoru na druhou ,
# vytvoř proměnnou kategorie, do které uložíš název kategorie odpovídající hodnotě BMI,
# vypiš výsledek do věty, jak je uvedeno níže:
# Martin tvé BMI je 20.0, což spadá do kategorie zdravá váha.

jmeno = 'Martin'
vaha = 80
vyska = 2
bmi = vaha / (vyska ** 2)
if bmi < 18.5:
    kategorie = 'podvýživa'
elif bmi >= 18.5 and bmi < 25:
    kategorie = 'zdravá váha'
elif bmi >= 25 and bmi < 30:
    kategorie = 'mírná nadváha'
elif bmi >= 30 and bmi < 40:
    kategorie = 'obezita'
else:
    kategorie = 'těžká obezita'
print(jmeno + ', tvé BMI je ' + str(bmi) + ', což spadá do kategorie', kategorie + '.')
print(f'{jmeno}, tvé BMI je {bmi}, což spadá do kategorie {kategorie}.')    # řešení od Milana

# Řešení - jiné než moje:

# Vstupní hodnoty uživatele
vyska = 2
vaha = 80
jmeno = 'Martin'
# Výpočet BMI
bmi = vaha / vyska ** 2
# Vytvoř proměnnou "kategorie", kam uložíš slovní ohodnocení BMI
if bmi > 40:
    kategorie = 'těžká obezita'
elif bmi > 30:
    kategorie = 'obezita'
elif bmi > 25:
    kategorie= 'mírná nadváha'
elif bmi > 18.5:
    kategorie = 'zdravá váha'
else:
    kategorie = 'podvýživa'
# Vytiskni odpoved s vysledkem
print(jmeno, "tvé BMI je", bmi, ", což spadá do kategorie", kategorie, ".")

####################################################
## Test Milan
####################################################

jmeno = input('Zadej jmeno: ')
vaha = input('Zadej vahu: ')
vyska = input('Zadej vysku: ')
bmi = int(vaha) / ((int(vyska) / 100) ** 2)

if bmi < 18.5:
    kategorie = 'podvýživa'
elif bmi >= 18.5 and bmi < 25:
    kategorie = 'zdravá váha'
elif bmi >= 25 and bmi < 30:
    kategorie = 'mírná nadváha'
elif bmi >= 30 and bmi < 40:
    kategorie = 'obezita'
else:
    kategorie = 'těžká obezita'

result = f'{jmeno}, tvé BMI je {bmi}, což spadá do kategorie {kategorie}.\n'
print(result)

with open('Milan_vaha.txt', 'a+', encoding='utf-8') as f:
    f.write(result)
