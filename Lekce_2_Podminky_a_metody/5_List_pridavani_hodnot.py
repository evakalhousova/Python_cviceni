# Vytvoř list zamestnanci, který bude obsahovat stringy 'František', 'Anna', 'Jakub', 'Klára',
# vypiš obsah zamestnanci za větu 'Zaměstnanci na začátku: ',
# vytvoř kopii listu zamestnanci a pojmenuj proměnnou zamestnanci_a,
# přidej do listu zamestnanci_a jména 'Bruno' a 'Anežka',
# vypiš obsah listu zamestnanci_a za string 'Nová jména přidána: ',
# vytvoř kopii listu zamestnanci a pojmenuj proměnnou zamestnanci_b,
# vlož jméno 'Bruno' na index 1,
# vypiš obsah proměnné zamestnanci_b za string: 'Nová jména vložena:'.

zamestnanci = ['František', 'Anna', 'Jakub', 'Klára']
print('Zaměstnanci na začátku:', zamestnanci)
zamestnanci_a = zamestnanci.copy()
zamestnanci_a.append('Bruno')
zamestnanci_a.append('Anežka')
print('Nová jména přidána:', zamestnanci_a)
zamestnanci_b = zamestnanci.copy()
zamestnanci_b.insert(1, 'Bruno')
print('Nová jména vložena:', zamestnanci_b)