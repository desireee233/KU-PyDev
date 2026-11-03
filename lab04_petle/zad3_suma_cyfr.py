# Lab 04 – Zadanie 3 (★): Suma i liczba cyfr
#
# Program wczytuje nieujemną liczbę całkowitą i wypisuje DOKŁADNIE:
#     Suma cyfr: 15
#     Liczba cyfr: 5
# (dla 12345).
#
# Rozwiąż to ARYTMETYCZNIE pętlą while, bez zamiany na tekst:
#   - n % 10 to ostatnia cyfra,
#   - n // 10 „odcina” ostatnią cyfrę.
# Uwaga: liczba 0 ma jedną cyfrę.

# TODO: Twój kod poniżej
a = int(input("Podaj nieujemną liczbę całkowitą: "))
suma = 0
liczba_cyfr = 0

while a > 0:
    suma += a % 10
    liczba_cyfr += 1
    a //= 10

print(f"Suma cyfr: {suma}")
print(f"Liczba cyfr: {liczba_cyfr}")