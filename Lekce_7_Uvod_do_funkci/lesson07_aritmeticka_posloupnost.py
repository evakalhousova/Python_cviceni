from typing import Optional, Tuple, List

def vygeneruj_arit_posloupnost(
        pocatecni_hodnota: int,
        krok: int,
        pocet_hodnot: int,
        vratit_sumu: bool = False
) -> Tuple[List[int], Optional[int]]:
    """
    Generuje aritmetickou posloupnost. 

    Parametry:
        pocatecni_hodnota (int): Zacatek posloupnosti. 
        krok (int): Krok posloupnosti.
        pocet_hodnot (int): Delka posloupnosti.
        vratit_sumu (bool): Spocitat a vratit sumu vygenerovane posloupnosti.

    Return:
        List[int]: Aritmeticka posloupnost.
        Optional[int]: Suma aritmeticke posloupnosti.

    Priklad:
        >>> vygeneruj_arit_posloupnost(2, 3, 5)
        [2, 5, 8, 11, 14]
        >>> vygeneruj_arit_posloupnost(2, 3, 5, vratit_sumu=True)
        ([2, 5, 8, 11, 14], 40)
    """
    hodnota = pocatecni_hodnota
    posloupnost = [pocatecni_hodnota]

    for _ in range(pocet_hodnot - 1):
        hodnota += krok
        posloupnost.append(hodnota)

    if vratit_sumu:
        suma = pocet_hodnot * (pocatecni_hodnota + hodnota)
        suma = int(suma/2)
        return posloupnost, suma
    return posloupnost, None
