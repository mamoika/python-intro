# Importowanie modułów
import math  # Moduł matematyczny

# Tworzenie list i łączenie ich za pomocą zip()
list_a = [1, 2, 3]
list_b = ['a', 'b', 'c']
zipped = zip(list_a, list_b)
print("Połączone listy:", list(zipped))  # Wynik: [(1, 'a'), (2, 'b'), (3, 'c')]

# Użycie funkcji z modułu math
number = 16
sqrt_number = math.sqrt(number)
print(f"Pierwiastek kwadratowy z {number} to {sqrt_number}")

# Obsługa wyjątku try-except
try:
    invalid_number = int("abc")  # Próba konwersji nieprawidłowego ciągu na liczbę
except ValueError as e:
    print("Błąd:", e)

# Linki do dokumentacji:
# zip(): https://docs.python.org/3/library/functions.html#zip
# math: https://docs.python.org/3/library/math.html
# ValueError: https://docs.python.org/3/library/exceptions.html#ValueError
