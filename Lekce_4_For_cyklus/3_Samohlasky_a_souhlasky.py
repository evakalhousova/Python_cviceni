# V této úloze vytvoř program, který spočítá kolik samohlásek a souhlásek obsahuje zadaný string:
# veta = 'Zvuk řeči je produkován poměrně otevřenou konfigurací vokálního traktu'
# Vytvoř proměnnou veta, typu str, která obsahuje hodnotu: "Zvuk řeči je produkován poměrně otevřenou konfigurací vokálního traktu",
# proměnnou samohlasky, typu str, která obsahuje 'aeiouáéíóú',
# proměnnou souhlasky, typu str, která obsahuje 'bcčdďfghjklmnňprřsštťvzžcdž',
# proměnnou vysledek, typu dict, který obsahuje klíče "souhlasky" a "samohlasky". Slovník bude evidovat výskyty těchto hodnot,
# iteraci přes všechny znaky v proměnné veta,
# pokud znak není ani samohláska, ani souhláska, tak jej přeskoč,
# pokud je znak samohláska nebo souhláska, inkrementuj ve slovníku vysledek správný klíč,
# nakonec vypiš konečný stav podle ukázky níže.
# Počet souhlásek: 35 | Počet samohlásek: 25

veta = 'Zvuk řeči je produkován poměrně otevřenou konfigurací vokálního traktu'
samohlasky = 'aeiouáéíóú'
souhlasky = 'bcčdďfghjklmnňprřsštťvzžcdž'
vysledek = {'souhlasky': 0, 'samohlasky': 0}
for znak in veta.lower():
    if znak not in samohlasky and znak not in souhlasky:
        continue
    elif znak in samohlasky:
        vysledek['samohlasky'] = vysledek.get('samohlasky') + 1
    else:
        vysledek['souhlasky'] = vysledek.get('souhlasky') + 1
print('Počet souhlásek:', vysledek.get('souhlasky'), '|', 'Počet samohlásek:', vysledek.get('samohlasky'))


# Jiné řešení:

# Zadaná proměnná
veta = 'Zvuk řeči je produkován poměrně otevřenou konfigurací vokálního traktu'
# Samohlásky & souhlásky
samohlasky = 'aeiouáéíóú'
souhlasky = 'bcčdďfghjklmnňprřsštťvzžcdž'
# Slovník s evidencí výskytu jednotlivých typů písmen
vysledek = {'souhlasky': 0, 'samohlasky': 0}
# Iterace přes zadanou proměnnou 'sentece'
for pismeno in veta:
    # .. pokud znak není písmeno
    if not pismeno.isalpha():
        continue
    # .. pokud je převedený znak mezi hodnotami samohlásek
    elif pismeno.lower() in samohlasky:
        vysledek['samohlasky'] += 1
    # .. pokud je převedený znak mezi hodnotami souhlásek
    elif pismeno.lower() in souhlasky:
        vysledek['souhlasky'] += 1
# Vypiš závěrečný výstup v podobě celkového počtu samohlásek a souhlásek
print(
    'Počet souhlásek:', vysledek['souhlasky'], '| Počet samohlásek:', vysledek['samohlasky']
)
