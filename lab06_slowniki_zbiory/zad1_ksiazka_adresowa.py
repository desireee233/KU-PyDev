# Lab 06 – Zadanie 1 (★): Książka adresowa
#
# Kontakty trzymaj w SŁOWNIKU: imię -> numer telefonu.
#
# Polecenia (każde w osobnej linii):
#     dodaj <imię> <telefon>  – dodaje albo nadpisuje kontakt, "Zapisano <imię>"
#     szukaj <imię>           – wypisuje numer albo "Brak kontaktu"
#     usuń <imię>             – usuwa kontakt albo "Brak kontaktu"
#     lista                   – wszystkie kontakty ALFABETYCZNIE, każdy w linii:  Adam: 500600700
#     koniec
#
# Wskazówki: contacts.get(name), del contacts[name], sorted(contacts.items())

contacts = {}

# TODO: Twój kod poniżej
a = input()
while a != "koniec":
    if a.startswith("dodaj"):
        _, name, phone = a.split()
        contacts[name] = phone
        print(f"Zapisano {name}")
    elif a.startswith("szukaj"):
        _, name = a.split()
        if name in contacts:
            print(contacts[name])
        else:
            print("Brak kontaktu")
    elif a.startswith("usuń"):
        _, name = a.split()
        if name in contacts:
            del contacts[name]
            print(f"Usunięto {name}")
        else:
            print("Brak kontaktu")
    elif a == "lista":
        for name, phone in sorted(contacts.items()):
            print(f"{name}: {phone}")
    else:
        print("Nieznane polecenie")
    a = input()