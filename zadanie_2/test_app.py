import unittest
from zadanie_2.app import is_valid_email, rectangle_area, filter_even_numbers, format_date, is_palindrome

class TestAppFunctions(unittest.TestCase):

    def test_is_valid_email(self):
        self.assertTrue(is_valid_email("test@example.com"))
        self.assertFalse(is_valid_email("invalid-email"))
        self.assertFalse(is_valid_email("missing@domain"))

    def test_rectangle_area(self):
        self.assertEqual(rectangle_area(5, 10), 50)
        self.assertRaises(ValueError, rectangle_area, -5, 10)

    def test_filter_even_numbers(self):
        self.assertEqual(filter_even_numbers([1, 2, 3, 4]), [2, 4])
        self.assertEqual(filter_even_numbers([]), [])

    def test_format_date(self):
        self.assertEqual(format_date("2025-04-05"), "05/04/2025")
        self.assertRaises(ValueError, format_date, "05-04-2025")

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertFalse(is_palindrome("Hello world"))

if __name__ == "__main__":
    unittest.main()
print("Import działa!")