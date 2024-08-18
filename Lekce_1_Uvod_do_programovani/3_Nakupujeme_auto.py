# Úloha musí splňovat následující:
# Vytvoř tyto proměnné:
# mercedes = 150_000
# rolls_royce = 400_000
# vybava = 50_000
# Slevu do proměnné sleva_merc a její hodnotu 5000,
# vypočítat cenu za dva Mercedesy, uložit ji do proměnné cena_2_merc ,
# vypočítat cenu za Mercedes a Rolls-Royce, uložit ji do proměnné cena_merc_a_rolls,
# vypočítat cenu za dva Rolls-Royce s příplatkovou výbavou (každý z nich), uložit ji do proměnné cena_2_rolls_s_vybavou,
# vypočítat cenu za Mercedes s příplatkovou výbavou, uložit ji do proměnné cena_merc_s_vybavou,
# vypočítat cenu po slevě Mercedesu a uložit ji do proměnné merc_se_slevou.
# Nakonec by měl program všechno přehledně vypsat.
# Ukázka
# Sleva na Mercedes: 5000
# Cena za dva Mercedesy je: 300000
# Cena za Mercedes a Rolls-Royce: 550000
# Cena za dva Rolls-Royce s příplatkovou výbavou: 900000
# Cena za Mercedes s příplatkovou výbavou: 200000
# Cena za Mercedes po slevě: 145000

mercedes = 150_000
rolls_royce = 400_000
vybava = 50_000
sleva_merc = 5000
cena_2_merc = mercedes * 2
cena_merc_a_rolls = mercedes + rolls_royce
cena_2_rolls_s_vybavou  = (rolls_royce + vybava) * 2
cena_merc_s_vybavou = mercedes + vybava
merc_se_slevou = mercedes - sleva_merc
print('Sleva na Mercedes:', sleva_merc)
print('Cena za dva Mercedesy je:', cena_2_merc)
print('Cena za Mercedes a Rolls-Royce:', cena_merc_a_rolls)
print('Cena za dva Rolls-Royce s příplatkovou výbavou:', cena_2_rolls_s_vybavou)
print('Cena za Mercedes s příplatkovou výbavou:', cena_merc_s_vybavou)
print('Cena za Mercedes po slevě:', merc_se_slevou)
