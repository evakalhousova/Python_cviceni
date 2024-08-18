cisla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
for cislo in cisla:
    if cislo % 3 == 0 and cislo % 5 == 0:
        print('FizzBuzz')
    elif cislo % 3 == 0:
        print('Fizz')
    elif cislo % 5 == 0:
        print ('Buzz')
    else:
        print(cislo)


for pismeno in ['a', 'b', 'c']:
    print(pismeno, end=" ")

obsah = [
    ['jmeno;prijmeni;email;projekt'],
    ['Matous;Holinka;m.holinka@firma.cz;hr'],
    ['Petr;Svetr;p.svetr@firma.cz;devops']
]
for radek in obsah:
    for bunka in radek:
        print(bunka)

for radek in obsah:
    print(radek)

    for bunka in radek[0].split(";"):
        print(bunka)


jmeno = 'Anna'
jmeno_2 = 'Eva'
if jmeno > jmeno_2:         # Srovnávání hodnot stringů (nemusí to být jen čísla)
    print(f'Ahoj {jmeno}, jak se vede? Já se jmenuju {jmeno_2}.')
else:
    print(jmeno_2)
