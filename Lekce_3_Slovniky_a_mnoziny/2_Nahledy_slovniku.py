# V této úloze si vyzkoušíš práci s nestovaným slovníkem. Jednotlivé kroky, které musí tvůj program obsahovat:
# Vytvoř proměnnou employees, typu dict s hodnotami: ... (viz řešení níže)
# vypiš všechny klíče ze zadaného slovníku employees s doplňujícím oznámením "Všechny klíče:",
# vypiš všechny hodnoty ze zadaného slovníku employees s doplňujícím oznámením "Všechny hodnoty:",
# vypiš jak klíče, tak hodnoty k zaměstnanci employee03 ze zadaného slovníku employees s doplňujícím oznámením "Všechny údaje k poslednímu zaměstnanci:".

employees = {
    'employee01': {
        'name': 'Marek',
        'surname': 'Parek',
        'email': 'marek.parek@gmail.com'
    },
    'employee02': {
        'name': 'Matous',
        'surname': 'Svatous',
        'email': 'matous.svatous@gmail.com'
    },
    'employee03': {
        'name': 'anna',
        'surname': 'rana',
        'email': 'anna.rana@gmail.com'
    }
}
print('Všechny klíče:', employees.keys())
print('Všechny hodnoty:', employees.values())
print('Všechny údaje k poslednímu zaměstnanci:', employees.get('employee03'))

#  Jiné řešení posledního řádku:
print("Všechny údaje k poslednímu zaměstnanci:", employees['employee03'].items())
