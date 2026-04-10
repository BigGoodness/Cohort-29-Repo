from unittest import TestCase
import book_suggestion_system

class book_suggestion_functions(TestCase):
    def test_for_show_all_books(self):
        books = ["The Hobbit," "The Mystery," "Brave Kind"]
        actual = book_suggestion_system.suggest_books(books)
        expected = 1
        self.assertEqual(actual, expected)
