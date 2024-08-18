# Zapiš uživ. funkci, která ověří zda operační systém na tvém pc je Windows či nikoliv.
# Tvůj zápis musí obsahovat:
# Definici a spuštění uživ. funkce je_os_windows,
# pomocnou knihovny sys s příslušnou metodou na ověření operačního systému,
# uživ. funkce je_os_windows, která vrátí hodnotu True, pokud pracuješ na op. systému windows. Jinak vrátí hodnotu False.
# Ukázka průběhu
# True  # pro Windows
# False  # pro Linux

import platform

def je_os_windows():
    return platform.system() == 'Windows'           # Vrátí hodnotu výrazu, tedy porovnání, výstup bude True nebo False.

print(je_os_windows())


# Jiné řešení:
import sys
def je_os_windows():
    """
    Vrať bool hodnotu True, pokud je můj os win. Jinak vrať False.
    """
    return sys.platform.startswith("win")
print(je_os_windows())
