# V této úloze vytvoř program, který vezme slovníky id123, id124 a id125 do našeho hlavního slovníku databaze. Jednotlivé kroky, které musí tvůj program obsahovat:
# Zapiš proměnné, se kterými budeš dál pracovat:
# id123 = {'jmeno': 'Thomas', 'vek': 45, 'zeme': 'Czechia', 'mesto': 'Brno'}
# id124 = {'jmeno': 'Daniel', 'vek': 34, 'zeme': 'Czechia', 'mesto': 'Prague'}
# id125 = {'jmeno': 'Eva', 'vek': 43, 'zeme': 'Czechia', 'mesto': 'Olomouc'}
# Vytvoř slovník databaze s klíči id123, id124, id125:
# databaze = {'id123': {},'id124': {},'id125': {}}
# přiřaď jednotlivé slovníky id123, id124, id125 ke konkrétním klíčům ve slovníku databaze,
# vypiš obsah slovníku databaze.

id123 = {'jmeno': 'Thomas', 'vek': 45, 'zeme': 'Czechia', 'mesto': 'Brno'}
id124 = {'jmeno': 'Daniel', 'vek': 34, 'zeme': 'Czechia', 'mesto': 'Prague'}
id125 = {'jmeno': 'Eva', 'vek': 43, 'zeme': 'Czechia', 'mesto': 'Olomouc'}
databaze = {'id123': {},'id124': {},'id125': {}}
databaze['id123'] = id123
databaze['id124'] = id124
databaze['id125'] = id125
print(databaze)
