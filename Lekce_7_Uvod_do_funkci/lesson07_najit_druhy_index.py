from typing import List, Optional

def najdi_druhy_index(seznam: List[int], hodnota: int) -> Optional[int]:
    """
    Najdi druhou pozici hodnoty v seznamu. Pokud hodnota neexistuje, vrati None.

    Parametry: 
        seznam (List[int]): Seznam, ve kterem se hleda urcita hodnota.
        hodnota (int): Cislo, pozici druheho vyskytu ktereho chceme najit.

    Return: 
        Optional[int]: Pokud se cislo objevuje v seznamu dvakrat a vic, 
        vrati se index jeho druhe pozice v seznamu. Jinak se vrati None.

    Priklad:
        >>> najdi_druhy_index([5, 6, 2, 2], 2)
        3
        >>> najdi_druhy_index([5, 6, 2, 2], 6)
        >>> najdi_druhy_index([5, 6, 2, 2, 6, 6], 6)
        4
    """
    pocet_hledani = 0
    for i, prvek in enumerate(seznam):
        if prvek == hodnota:
            pocet_hledani += 1
            if pocet_hledani > 1:
                return i
    return None


if __name__ == "__main__":
    ...
    # print(najdi_druhy_index([5, 6, 2, 2], 2))
    # print(najdi_druhy_index([5, 6, 2, 2], 6))
    # print(najdi_druhy_index([5, 6, 2, 2, 6, 6], 6))