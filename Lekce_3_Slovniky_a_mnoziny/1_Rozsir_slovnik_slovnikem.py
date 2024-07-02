# Vytvoří nový prázdný slovník user_1,
# doplní do slovníku user_1 klíč name (hodnota Marek) a surname (hodnota Parek),
# pomocí vhodné metody rozšíří stávající slovník user_1 o zadanou proměnnou user_email,
# vypiš hodnoty nového slovníku user_1 s úvodním textem User #01:.

user_1 = {}
user_1['name'] = 'Marek'
user_1['surname'] = 'Parek'
user_1.update({'user_email': 'marek.parek@gmail.com'})
print('User #01:', user_1)

# Jiné řešení:
user_1 = {}
user_1['name'] = 'Marek'
user_1['surname'] = 'Parek'
user_email = {'email': 'marek.parek@gmail.com'}
user_1.update(user_email)
print('User #01:', user_1)
