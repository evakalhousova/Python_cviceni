# V této úloze si vyzkoušíš identifikaci anagramů.
# Anagramy jsou dvě a více slov složených ze stejných znaků. Třeba anglická slova ship a hips.
# Tvoje úloha musí obsahovat tyto kroky:
# Vytvoř funkci je_anagram, která může mít jako vstup libovolně dlouhý tuple,
# z první hodnoty v sekvenci stanoví vzor, jehož písmena seřadí,
# funkce potom projde všechny hodnoty ze vstupu a ověří, jestli nejsou anagram,
# pokud JSOU anagram, vrátí True,
# pokud NEJSOU anagram, vrátí False,
# vyzkoušej funkci spustit podle zadání v ukázce.
# Ukázka průběhu:
# print(
    # je_anagram("ship", "hips", "phis"),
    # je_anagram("ship", "hips", "duck"),
    # sep="\n"
# )
# Vypíše tyto výstupy:
# True
# False

def je_anagram(*args: tuple):
    vzor = args[0]
    serazeny_vzor = ''.join(sorted(vzor))
    for slovo in args:
        serazene_slovo = ''.join(sorted(slovo))
        if serazeny_vzor == serazene_slovo:
            vysledek = True
        else:
            vysledek = False
            break
    return vysledek

print(
    je_anagram("ship", "hips", "phis"),
    je_anagram("ship", "hips", "duck"),
    sep="\n"
)

#Jiné řešení:
def je_anagram(*args) -> bool:
    """
    Vrati boolean True, pokud jsou vsechny parametry anagramy.
    Jinak vrati False.
    Priklad:
    print(je_anagram("ship", "hips", "hisp"))
    True
    print(je_anagram_matous("ship", "hips", "duck"))
    False
    """
    vzor = sorted(args[0])
    for slovo in args:
        if sorted(slovo) != vzor:
            return False
    else:
        return True
print(
    je_anagram("ship", "hips", "hisp"),
    je_anagram("ship", "hips", "duck"),
    sep="\n"
)
