cislo = 15

zbytek_3 = cislo % 3
zbytek_5 = cislo % 5
if zbytek_3 == 0 and zbytek_5 == 0:
    print("FizzBuzz")
elif zbytek_3 == 0:
    print("Fizz")
elif zbytek_5 == 0:
    print("Buzz")
else:
    print(cislo)
