import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))
def rectangle_area(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Długość i szerokość muszą być większe od zera.")
    return length * width
def filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]
from datetime import datetime

def format_date(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.strftime("%d/%m/%Y")
    except ValueError:
        raise ValueError("Nieprawidłowy format daty. Oczekiwano YYYY-MM-DD.")
def is_palindrome(text):
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]
