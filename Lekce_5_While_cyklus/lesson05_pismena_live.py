pismena = ["a", "a", "b", "c", "d", "a", "e", "g", "m"]


while pismena:
    print("Pismena:", ", ".join(pismena))
    zadani = input("Ktere pismeno chces vyhodit?")

    while zadani in pismena:
        pismena.remove(zadani)