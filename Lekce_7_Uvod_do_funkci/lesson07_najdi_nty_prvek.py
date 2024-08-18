from typing import List, Optional, Union


def najdi_nty_index(seznam: List[int], 
                     hodnota: int, 
                     min_pocet_vyskytu: int) -> Union[Optional[int], None]:
    """
    Najdi n-tou pozici hodnoty v seznamu. Pokud hodnota neexistuje, vrati None.

    Parametry: 
        seznam (List[int]): Seznam, ve kterem se hleda urcita hodnota.
        hodnota (int): Cislo, pozici n-teho vyskytu ktereho chceme najit.
        min_pocet_vyskytu (int): kolikrat se cislo musi objevit v seznamu.

    Return: 
        Optional[int]: Pokud se cislo objevuje v seznamu dvakrat a vic, 
        vrati se index jeho n-te pozice v seznamu. Jinak se vrati None.

    Priklad:
        >>> najdi_nty_index([5, 6, 2, 2], 2, 2)
        3
        >>> najdi_nty_index([5, 6, 2, 2], 6, 2)
        >>> najdi_nty_index([5, 6, 2, 2, 6, 6], 6, 3)
        5
        >>> najdi_nty_index([6, 5, 2, 2, 6, 6], 6, 1)
        0
    """
    if type(seznam[0]) != type(hodnota):
        print("Spatny datovy typ pro parametr `hodnota`!")
        return None
    
    pocet_hledani = 0
    for i, prvek in enumerate(seznam):
        if prvek == hodnota:
            pocet_hledani += 1
            if pocet_hledani >= min_pocet_vyskytu:
                return i
    return None


if __name__ == "__main__":
    pass
    # print(najdi_druhy_index([5, 6, 2, 2], 2))
    # print(najdi_druhy_index([5, 6, 2, 2], 6))
    # print(najdi_druhy_index([5, 6, 2, 2, 6, 6], 6)