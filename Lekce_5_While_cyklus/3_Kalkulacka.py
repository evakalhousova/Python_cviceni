# V této úloze vytvoř program, který si od uživatele nejprve vyžádá aritmetický operátor a následně čísla, se kterými celý zápis vypočítá.
# Po každé operaci se program uživatele zeptá zda chce provést další operaci nebo chce program ukončit.
# Jednotlivé kroky, které program musí obsahovat:
# Vytvoř nekonečnou smyčku
# uživatel může vybrat operátor, dostupné jsou "+", "-",
# vstup uživatele ulož do proměnné operation,
# pokud hodnota v proměnné operation není ("+", "-"), vypiš "Nezadali jste platný operátor, zkuste to znovu" a vrátí se na začátek běhu programu,
# pokud je hodnota v proměnné - ("+", "-"), dovol uživateli zadat vstupy do proměnných number_1 a number_2,
# spoj hodnoty v number_1, choice a number_2, vypočítej výsledek a vypiš např. 1 + 9 = 10,
# zeptá se uživatele zda chce provést další operaci pokud ano program se vrátí na začátek běhu, pokud ne program se ukončí.
# Ukázky průběhů:
# Sčítání:    "+",
# Odčítání:   "-",
# ----------------------
# Vyber si operaci: +
# Zadej první číslo: 1
# Zadej druhé číslo: 1
# 1 + 1 = 2
# Chcete provést další operaci?('a' pro ano, jakákoliv jiná klávesa pro ne):
# Sčítání:    "+",
# Odčítání:   "-",
# ----------------------
# Vyber si operaci: /
# Nezadali jste platný operátor, zkuste to znovu.

operator = ['+', '-']           # Je třeba pracovat s indexy pro + a -?
print('Sčítání:    "+"')
print('Odčítání:   "-"')
print('-' * 22)
while True:
    operation = input('Vyber si operaci:')
    if operation not in operator:
        print("Nezadali jste platný operátor, zkuste to znovu.")
    else:
        number_1 = int(input('Zadej první číslo:'))
        number_2 = int(input('Zadej druhé číslo:'))
        if operation == operator[0]:
            result_addition = number_1 + number_2
            print(number_1, operation, number_2, '=', result_addition)
        else:
            result_subtraction = number_1 - number_2
            print(number_1, operation, number_2, '=', result_subtraction)
        question = input("Chcete provést další operaci?('a' pro ano, jakákoliv jiná klávesa pro ne):")
        if question == 'a':
            continue
        else:
            break


# Jiné řešení:

# Zapiš nekonečnou smyčku pomocí proměnné `mod`
while True:
    # Zapiš výběr operace, kterou kalkulačka disponuje
    operation = input('''
Sčítání:    "+"
Odčítání:   "-"
----------------------
Vyber si operaci: '''
                )
    # Ověř zda uživatel zvolil platný operátor
    if operation not in ('+','-'):
        print('Nezadali jste platný operátor, zkuste to znovu.')
        continue
    # Získej čísla pro výpočet od uživatele
    number_1 = int(input('Zadej první číslo: '))
    number_2 = int(input('Zadej druhé číslo: '))
    # Dle operátoru proveď výpočet a vypiš ho
    if operation == '+':
        print(f'{number_1} + {number_2} = {number_1 + number_2}')
    elif operation == '-':
        print(f'{number_1} - {number_2} = {number_1 - number_2}')
    # Ověř zda chce uživatel pokračovat nebo chce program ukončit
    again = input('Chcete provést další operaci?(a pro ano, jakákoliv jiná klávesa pro ne): ')
    if again == 'a':
        continue
    else:
        print('Ukončuji...')
        break
