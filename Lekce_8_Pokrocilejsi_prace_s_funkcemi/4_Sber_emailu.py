# Vytvoř program, který ze zadaného textu vytáhne emaily.
# Tvoje úloha musí obsahovat tyto kroky:
# Vytvoř proměnnou text a ulož do proměnné
# text = """\
# Lorem ... aliquet.                            # Celý text viz níže
# """
# vytvoř funkci uloz_emailove_adresy, funkce bude mít jeden parameter text, vezme zadaný text a vytáhne z něj všechny emailové adresy,
# výstup z funkce, vrať do proměnné vysledek,
# vypiš obsah proměnné vysledek podle ukázky níž.
# Ukázka průběhu
# ['tiger123@email.cz', 'cnn@info.com', 'abc@gmail.com', 'b2b@money.fr', 'spam@info.cz']

text = """\
Lorem ipsum dolor sit amet, consectetur adipiscing
elit. Mauris vulputate lacus id eros consequat tempus.
Nam viverra velit sit amet lorem lobortis, at tincidunt
nunc ultricies. Duis facilisis ultrices lacus, id
tiger123@email.cz auctor massa molestie at. Nunc tristique
fringilla congue. Donec ante diam cnn@info.com, dapibus
lacinia vulputate vitae, ullamcorper in justo. Maecenas
massa purus, ultricies a dictum ut, dapibus vitae massa.
Cras abc@gmail.com vel libero felis. In augue elit, porttitor
nec molestie quis, auctor a quam. Quisque b2b@money.fr
pretium dolor et tempor feugiat. Morbi libero lectus,
porttitor eu mi sed, luctus lacinia risus. Maecenas posuere
leo sit amet spam@info.cz. elit tincidunt maximus. Aliquam
erat volutpat. Donec eleifend felis at leo ullamcorper cursus.
Pellentesque id dui viverra, auctor enim ut, fringilla est.
Maecenas gravida turpis nec ultrices aliquet.
"""

# Moje řešení to nevzalo, ale podle mě funguje.

def uloz_emailove_adresy(vlozeny_text):
    adresy = []
    rozdeleny_text = vlozeny_text.split()
    for slovo in rozdeleny_text:
        if '@' in slovo and '.' in slovo:
            adresy.append(slovo)
    return adresy

vysledek = uloz_emailove_adresy(text)
print(vysledek)


# Jiné řešení:
# Vytvor promennou text a uloz do ni zadany text
text = '''\
Lorem ipsum dolor sit amet, consectetur adipiscing
elit. Mauris vulputate lacus id eros consequat tempus.
Nam viverra velit sit amet lorem lobortis, at tincidunt
nunc ultricies. Duis facilisis ultrices lacus, id
tiger123@email.cz auctor massa molestie at. Nunc tristique
fringilla congue. Donec ante diam cnn@info.com, dapibus
lacinia vulputate vitae, ullamcorper in justo. Maecenas
massa purus, ultricies a dictum ut, dapibus vitae massa.
Cras abc@gmail.com vel libero felis. In augue elit, porttitor
nec molestie quis, auctor a quam. Quisque b2b@money.fr
pretium dolor et tempor feugiat. Morbi libero lectus,
porttitor eu mi sed, luctus lacinia risus. Maecenas posuere
leo sit amet spam@info.cz. elit tincidunt maximus. Aliquam
erat volutpat. Donec eleifend felis at leo ullamcorper cursus.
Pellentesque id dui viverra, auctor enim ut, fringilla est.
Maecenas gravida turpis nec ultrices aliquet.
'''
def uloz_emailove_adresy(text: str) -> list:
    """
    Uloz vsechny ocistene emailove adresy ze zadaneho textu.
    Priklad:
    print(uloz_emailove_adresy("Ahoj, tady matous@gmail.com."))
    {'matous@gmail.com'}
    print(uloz_emailove_adresy("Ahoj, tady matous"))
    {}
    """
    return [
        slovo.strip(",.:;")
        for slovo in text.split()
        if "@" in slovo
    ]
# Uloz vystup funkce do promenne
vysledek = uloz_emailove_adresy(text)
# Vytiskni obsah promenne vysledek
print(vysledek)
