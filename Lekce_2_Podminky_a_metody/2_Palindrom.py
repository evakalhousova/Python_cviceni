# Vytvoř list zadana_slova, který obsahuje hodnoty: ["jaro", "jej", "kolo", "aha"]
# vyber libovolné slovo z listu zadana_slova a ulož jej do proměnné slovo (pomocí indexu),
# pokud se jedná o palindrom, vypsat "Slovo '<slovo>' je palindrom!",
# pokud se nejedná o palindrom, vypsat - "Slovo '<slovo>' není palindrom".

zadana_slova = ["jaro", "jej", "kolo", "aha"]
slovo = zadana_slova[0]
print('Zadej slovo:', slovo)
if slovo == slovo[::-1]:
    print("Slovo", "'" + slovo + "'", "je palindrom!")
else:
    print("Slovo", "'" + slovo + "'", "není palindrom.")


# Řešení - jiné než moje:

# Zadaná slova
zadana_slova = ["jaro", "jej", "kolo", "aha"]

# Vstup uživatele
slovo = "jaro"

# Zkontroluj hodnotu
if slovo == slovo[::-1]:
    # pokud se jedná o palindrom
    print("Slovo '" + slovo + "' je palindrom!")

else:
    # pokud se nejedná o palindrom
    print("Slovo '" + slovo + "' není palindrom.")