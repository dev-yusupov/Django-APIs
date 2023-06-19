from django.test import TestCase
from django.urls import reverse
from .models import Book

# Create your tests here.
class BookTests(TestCase):
    """Test cases for Book Model"""

    @classmethod
    def setUpTestData(self):
        self.book = Book.objects.create(
            title = "Test Title",
            subtitle = "Test subtitle",
            author = "Test Testov",
            isbn = "1234567891011"
        )
    
    def test_book_content(self):
        self.assertEqual(self.book.title, "Test Title")
        self.assertEqual(self.book.subtitle, "Test subtitle")
        self.assertEqual(self.book.author, "Test Testov")
        self.assertEqual(self.book.isbn, "1234567891011")
    
    def test_book_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "subtitle")
        self.assertTemplateUsed(response, "index.html")