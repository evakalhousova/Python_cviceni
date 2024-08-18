# V této úloze vytvoř program, který:
# Uloží hodnotu "Lukáš", do proměnné jmeno,
# uloží hodnotu "Dvořák", do proměnné prijmeni,
# vytvoří proměnnou cele_jmeno, do které spojíš hodnoty v proměnných jmeno a prijmeni oddělené mezerou,
# vytvoří proměnnou delka_jmena, která bude obsahovat délku hodnoty v proměnné cele_jmeno (započítej i přidanou mezeru),
# vypíše hodnotu v proměnné delka_jmena (doplněnou stringem "Délka jména:"),
# vypíše proměnnou cele_jmeno, která bude shora i zespoda ohraničená řadami rovnítek.
# pozn. k ohraničení použij operaci opakování, znak = použij v každé řadě tolikrát, kolik znaků obsahuje string uložený v proměnné cele_jmeno.
# Ukázka průběhu:
# Celé jméno: Lukáš Dvořák
# Délka jména: 12
# ==========
# Lukáš Dvořák
# ==========

jmeno = 'Lukáš'
prijmeni = 'Dvořák'
cele_jmeno = jmeno + ' ' + prijmeni
delka_jmena = len(cele_jmeno)
print('Celé jméno:', cele_jmeno)
print('Délka jména:', delka_jmena)
print('=' * delka_jmena)
print(cele_jmeno)
print('=' * delka_jmena)
