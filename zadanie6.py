# Zadanie 6

import random

odleglosc = random.randint(100, 200)
srednieSpalanie = float(input('Podaj średnie spalanie w l. na 100 km.: ')) # 6 litrow
Cena = float(input('Podaj aktualną cenę paliwa za litr: '))

wynikPrzewidywaneZuzycie = srednieSpalanie * odleglosc / 100
wynikKosztPodrozy = Cena * wynikPrzewidywaneZuzycie
print(f'Odleglość: {odleglosc} km.')
print(f'Przewidywane zużycie paliwa: {wynikPrzewidywaneZuzycie} l.')
print(f'Szacowane koszty podróży: {wynikKosztPodrozy:.2f} zł.')