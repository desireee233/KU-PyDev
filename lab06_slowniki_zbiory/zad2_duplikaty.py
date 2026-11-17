# Lab 06 – Zadanie 2 (★): Usuwanie duplikatów
#
# Program wczytuje słowa oddzielone spacjami i wypisuje DOKŁADNIE
# (dla danych  a b a c b a):
#     Bez duplikatów: a b c                   <- kolejność pierwszych wystąpień
#     Usunięto: 3                             <- ile słów odrzucono
#     Unikalne (alfabetycznie): a b c         <- zbiór (set) posortowany
#
# Wskazówka: do pilnowania „czy już widziałem to słowo” użyj zbioru seen = set().
# Sprawdzanie  x in seen  w zbiorze jest dużo szybsze niż w liście.

# TODO: Twój kod poniżej
a = input().split()
seen = set()
unique_words = []
removed_count = 0
for word in a:
    if word not in seen:
        seen.add(word)
        unique_words.append(word)
    else:
        removed_count += 1
        print("bez duplikatów:", " ".join(unique_words))
        print("usunięto:", removed_count)
        print("unikalne (alfabetycznie):", " ".join(sorted(seen)))