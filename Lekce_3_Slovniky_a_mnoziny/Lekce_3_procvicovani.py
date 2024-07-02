muj_slovnik = dict()
muj_slovnik['jméno'] = 'Eva'
print(muj_slovnik)

muj_slovnik_2 = {'jméno': 'Eva', 'věk': 32, 'řidičské oprávnění': True}
print(muj_slovnik_2)
kontakty = {'mobil': 606123123, 'e-mail': 'test@gmail.com'}
muj_slovnik_2['kontaktní údaje'] = kontakty
print(muj_slovnik_2)

print(muj_slovnik_2['kontaktní údaje'])
print(muj_slovnik_2['kontaktní údaje']['e-mail'])
