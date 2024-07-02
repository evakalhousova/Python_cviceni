# Na záčatku nachystá tyto proměnné:
# kandidati = ['Bruno', 'Anežka']
# zamestnanci = ['František', 'Bruno', 'Anna', 'Jakub', 'Klára']
# vytvoří proměnnou bez_bruna, kam přiřadí hodnoty z proměnné kandidati,
# odstraní z listu bez_bruna string 'Bruno',
# vypíše obsah proměnné bez_bruna za string: 'Bruno odstraněn:',
# zopakuje a uloží třikrát obsah listu bez_bruna do proměnné opakovani_kandidati,
# vypíše obsah proměnné opakovani_kandidati za string: 'Opakování kandidáti:',
# spojí list zamestnanci s listem opakovani_kandidati do nového listu spojeni_zamestnanci,
# vypíše obsah nového listu spojeni_zamestnanci za string: 'Spojeni zaměstnanci:'

kandidati = ['Bruno', 'Anežka']
zamestnanci = ['František', 'Bruno', 'Anna', 'Jakub', 'Klára']
bez_bruna = kandidati.copy()
bez_bruna.remove('Bruno')
print('Bruno odstraněn:', bez_bruna)
opakovani_kandidati = bez_bruna * 3
print('Opakovaní kandidáti:', opakovani_kandidati)
spojeni_zamestnanci = zamestnanci + opakovani_kandidati
print('Spojení zaměstnanci:', spojeni_zamestnanci)