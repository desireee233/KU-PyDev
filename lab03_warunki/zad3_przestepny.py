# Lab 03 – Zadanie 3 (★): Rok przestępny
#
# Rok jest przestępny, gdy:
#   - dzieli się przez 4 i NIE dzieli się przez 100,
#   - albo dzieli się przez 400.
#
# Wypisz dokładnie jedno z dwóch zdań:
#     Rok 2024 jest przestępny
#     Rok 2023 nie jest przestępny
#
# Wskazówka: warunek zapiszesz w jednej linii z and / or.

# TODO: Twój kod poniżej
a = int(input("Podaj rok: "))
if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
    print(f"Rok {a} jest przestępny")
else:
    print(f"Rok {a} nie jest przestępny")
    