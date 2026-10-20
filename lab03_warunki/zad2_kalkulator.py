# Lab 03 – Zadanie 2 (★): Kalkulator z wyborem działania
#
# Program wczytuje kolejno: liczbę, operator (+, -, *, /) i drugą liczbę,
# a potem wypisuje wynik, np.:  8.0 * 2.0 = 16.0
#
# Obsłuż przypadki szczególne instrukcją if:
#   - dzielenie przez zero  -> "Nie można dzielić przez zero"
#   - inny operator         -> "Nieznany operator"

# TODO: Twój kod poniżej
a = float(input("Podaj pierwszą liczbę: "))
operator = input("Podaj operator (+, -, *, /): ")
b = float(input("Podaj drugą liczbę: "))
if operator == "+":
    result = a + b
    print(f"{a} + {b} = {result}")
elif operator == "-":
    result = a - b
    print(f"{a} - {b} = {result}")
elif operator == "*":
    result = a * b
    print(f"{a} * {b} = {result}")
elif operator == "/":
    if b == 0:
        print("Nie można dzielić przez zero")
    else:
        result = a / b
        print(f"{a} / {b} = {result}")
else:
    print("Nieznany operator")