# V této úloze vytvoř program, který:
# Vytvoří proměnné:
# cisla_1 = {1, 2, 3, 4}
# cisla_2 = {3, 4, 5, 6}
# zjistí jaké hodnoty prvního setu jsou rozdílné oproti setu druhému a uloží hodnoty do proměnné rozdil_cisel,
# vypíše výsledek s ohlášením "Rozdílné hodnoty prvního setu oproti druhému:".

cisla_1 = {1, 2, 3, 4}
cisla_2 = {3, 4, 5, 6}
rozdil_cisel = cisla_1.difference(cisla_2)  # jiné řešení:  rozdil_cisel = cisla_1 - cisla_2
print('Rozdílné hodnoty prvního setu oproti druhému:', rozdil_cisel)
