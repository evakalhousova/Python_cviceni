

def zobraz_nabidku(args):
    
    vyber = " | ".join(args)
    oddelovac = "-" * len(vyber)
    print(oddelovac, vyber, oddelovac, sep="\n")

def clear_output():
    """
    Clears the terminal based on the user platform.
    """


def vypocitej_zakladni_op():
    zapis = "("

    while (hodnota := input("Vstup:")):
        if hodnota.isnumeric():
            zapis += str(hodnota)
        elif hodnota in ("+", "-","*", "/"):
            zapis += str(hodnota)
        elif hodnota == "=":
            zapis += ")"
            vysledek = eval(zapis)
            print("Vysledek:", vysledek)
            break

def vypocitej_prumer():
    rada_cisel = []

    while (hodnota := input("Vstup:")) != "=":
        if hodnota.isnumeric():
            rada_cisel.append(int(hodnota))
    
    vysledek = sum(rada_cisel) / len(rada_cisel)
    print("Vysledek:", vysledek)



def vypocitej_mocninu():
    zaklad = input("zaklad:")
    exponent = input("exponent:")

    vysledek = int(zaklad) ** int(exponent)
    print("Vysledek:", vysledek)


def kalkulacka():
    operace = ("+", "-", "*", "/", "prum", "pow", "quit")

    while ...:
        zobraz_nabidku(operace)
        vyber = input("VYBER OPERACI:")

        # clear_output()
        if vyber == "quit":
            print("Ukoncuji kalkulacku")
            break
        elif vyber in ("+", "-", "*", "/"):
            vypocitej_zakladni_op()
        elif vyber == "prum":
            vypocitej_prumer()
        elif vyber == "pow":
            vypocitej_mocninu()
        


if __name__ == "__main__":
    kalkulacka()