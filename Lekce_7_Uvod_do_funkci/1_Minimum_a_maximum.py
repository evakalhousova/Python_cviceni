# Pomocí dostupných zabudovaných funkcí zjisti ze zadaného seznamu muj_seznam minimální a maximální hodnotu.
# Jednotlivé kroky, které program musí obsahovat:
# Vytvoř proměnnou muj_seznam, která odkazuje na hodnotu typu list: [43, 45, 87, 21, 23],
# uložit pomocí vhodných funkcí hodnoty do proměnných minimum a maximum,
# pomocí jednoho výstupu vypsat obě hodnoty (viz. ukázka).
# Ukázka průběhu
# Minimální hodnota je 21. Maximální hodnota je 87.

muj_seznam = [43, 45, 87, 21, 23]
minimum = min(muj_seznam)
maximum = max(muj_seznam)
print(f'Minimální hodnota je {minimum}. Maximální hodnota je {maximum}.')           # Jiné řešení: print("Minimální hodnota je", minimum, ". Maximální hodnota je", maximum, ".")
