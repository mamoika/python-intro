# Praca z plikami i obsługa wyjątków

# Ścieżka do pliku
file_path = "example.txt"

try:
    # Otwieranie i czytanie zawartości pliku
    with open(file_path, "r") as file:
        content = file.readlines()
        print("Zawartość pliku:")
        for line in content:
            print(line.strip())
    
    # Liczenie liczby linii i słów
    num_lines = len(content)
    num_words = sum(len(line.split()) for line in content)
    print(f"\nLiczba linii: {num_lines}")
    print(f"Liczba słów: {num_words}")

except FileNotFoundError:
    print(f"Błąd: Plik '{file_path}' nie istnieje.")
except Exception as e:
    print(f"Wystąpił nieoczekiwany błąd: {e}")
