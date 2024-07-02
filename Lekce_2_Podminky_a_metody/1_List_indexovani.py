# Vytvoří list zamestnanci, který obsahuje hodnoty: ['František', 'Bruno', 'Anna', 'Jakub', 'Klára', 'Anežka', 'Anežka', 'Anežka']
# Ulož poslední index ze zadaného listu zamestnanci do proměnné posledni_index,
# Vypiš jméno na indexu 2 za string: 'Na indexu 2 je: ',
# vypiš jméno na posledním indexu za string: 'Na <posledni_index> indexu je:',
# vypiš jména od indexu 2 do 5 za string: 'V intervalu od 2 do 5 je:',
# vypiš každý třetí prvek listu zamestnanci počínaje hodnotou 'František' za string: 'Každý třetí člen je:'.

zamestnanci = ['František', 'Bruno', 'Anna', 'Jakub', 'Klára', 'Anežka', 'Anežka', 'Anežka']
posledni_index = len(zamestnanci) -1
print('Na indexu 2 je:', zamestnanci[2])
print('Na', posledni_index, 'indexu je:', zamestnanci[posledni_index])
print('V intervalu od 2 do 5 je:', zamestnanci[2:6])
print('Každý třetí člen je:', zamestnanci[::3])