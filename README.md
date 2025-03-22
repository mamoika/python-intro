# python-intro
Wyszukanie zagadnień w dokumentacji Pythona
a) Funkcja wbudowana: zip()
Opis: Funkcja zip() służy do łączenia elementów z dwóch lub więcej iterowalnych obiektów (np. list, krotek) w krotki. Tworzy iterator par (lub większej liczby elementów), który można przekształcić np. w listę. Jeśli obiekty mają różną długość, wynik jest obcięty do najkrótszego z nich.

Przykład: zip([1, 2], ['a', 'b']) zwraca iterator par: (1, 'a'), (2, 'b').

Link: Dokumentacja Pythona - zip()

b) Moduł standardowy: random
Opis: Moduł random dostarcza funkcje do generowania liczb losowych i operacji losowych. Przykładowe funkcje to random.random() (losowa liczba od 0 do 1), random.randint(a, b) (losowa liczba całkowita w przedziale [a, b]) czy random.shuffle() (losowe mieszanie listy).

Przykład: random.randint(1, 10) generuje losową liczbę całkowitą od 1 do 10.

Link: Dokumentacja Pythona - random

c) Wyjątek: ValueError
Opis: Wyjątek ValueError jest zgłaszany, gdy funkcja otrzyma argument o poprawnym typie, ale nieprawidłowej wartości. Przykładem może być próba konwersji ciągu znaków na liczbę, gdy ciąg nie reprezentuje liczby (np. int("abc")).

Przykład: int("xyz") zgłasza ValueError.

Link: Dokumentacja Pythona - ValueError

