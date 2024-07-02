# V této úloze vytvoř program, který se pokusí ověřit, jestli heslo vložené uživatelem patří k jeho účtu. Jednotlivé kroky, které program musí obsahovat:
# Nejprve vytvoř proměnné:
# jmeno = 'Marek'
# heslo = '1234'
# uzivatel = {'Marek': '1234'}
# zapiš podmínku, která zkontroluje, jestli se hodnoty v proměnných jmeno a heslo shodují s klíčem a hodnotou ve slovníku uzivatel,
# pokud se shodují vypiš oznámení jako v ukázce níže,
# pokud se neshodují, opět vypiš oznámení jako v ukázce níže.
# Hodnoty v proměnných se shodují: Ahoj Marek vítej v aplikaci! Pokračuj...
# Pokud se neshoduje buď proměnná `jmeno`, nebo proměnná `heslo`: Uživatelské jméno nebo heslo nejsou v pořádku!

jmeno = 'Marek'
heslo = '1234'
uzivatel = {'Marek': '1234'}
uzivatel_keys = list(uzivatel.keys())
if jmeno == uzivatel_keys[0] and heslo == uzivatel.get('Marek'):
    print('Ahoj', jmeno, 'vítej v aplikaci! Pokračuj...')
else:
    print('Uživatelské jméno nebo heslo nejsou v pořádku!')

# Jiné řešení - Engeto studijní materiály:

# Uložené přihlašovací údaje
jmeno = 'Marek'
heslo = '1234'
uzivatel = {'Marek': '1234'}
# Ověř jestli zadané jméno a heslo souhlasí s uloženými údaji ve sl. "uzivatel"
if uzivatel.get(jmeno) == heslo:
    # ... pokud SOUHLASÍ, přivítej uživatele jménem
    print("Ahoj", jmeno, "vítej v aplikaci! Pokračuj...")
else:
    # ... pokud NESOUHLASÍ, upozorni uživatele o omylu
    print("Uživatelské jméno nebo heslo nejsou v pořádku!")
