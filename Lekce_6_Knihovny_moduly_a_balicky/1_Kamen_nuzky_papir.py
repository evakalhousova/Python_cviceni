# Pro tuto úlohu budeš potřebovat nahrát knihovnu random. Tvým úkolem bude napsat hru kámen, nůžky, papír.
# Program musí obsahovat:
# Naimportuj modul random,
# vytvoř list moznosti s hodnotami 'kamen', 'nuzky', 'papir',
# vytvoř proměnnou hrac a ulož do ní hodnotu "kamen",
# vytvoř proměnnou pocitac, které bude náhodně přiřazen prvek z listu moznosti
# pokud hráč vyhraje, vypiš "Vyhrál jsi!", pokud prohraje, vypíš "Prohrál jsi:(", v případě remízy vytiskni "Nerozhodně".

import random
moznosti = ['kámen', 'nůžky', 'papír']
hrac = 'kámen'
pocitac = random.choice(moznosti)
print('Hráč: ', hrac)
print('Počítač: ', pocitac)
if hrac == 'kámen' and pocitac == 'nůžky':
    print('Vyhrál jsi!')
elif hrac == 'nůžky' and pocitac == 'papír':
    print('Vyhrál jsi!')
elif hrac == 'papír' and pocitac == 'kámen':
    print('Vyhrál jsi!')
elif pocitac == hrac:
    print('Nerozhodně.')
else:
    print('Prohrál jsi. :(')
