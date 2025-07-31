import unittest
from app import app

class BookInfoTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_missing_title_parameter(self):
        response = self.app.get('/book')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Please provide a book title", response.data)

    def test_valid_book_title(self):
        response = self.app.get('/book?title=To Kill a Mockingbird')
        self.assertEqual(response.status_code, 200)
        self.assertIn('title', response.json)
        self.assertIn('author', response.json)

    def test_valid_title_returns_data(self):
        response = self.app.get('/book?title=To Kill a Mockingbird')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('title', data)
        self.assertIn('author', data)
        self.assertIn('first_publish_year', data)
        self.assertIsInstance(data['subjects'], list)

    def test_title_not_found(self):
        response = self.app.get('/book?title=SomeRandomNonexistentBookTitle1234')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b"No books found", response.data)

    def test_title_with_special_characters(self):
        response = self.app.get("/book?title=Harry Potter & the Sorcerer's Stone")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('title', data)

if __name__ == '__main__':
    unittest.main()