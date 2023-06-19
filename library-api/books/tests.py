from django.test import TestCase
from .models import Book

"""Modules of Rest Framework to test API"""
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.
class BookModelTests(TestCase):
    """Test cases for Book model."""

    @classmethod
    def setUpTestData(self):
        self.book = Book.objects.create(
            title = "Test Title",
            subtitle = "Exelent test subtitle",
            author = "Test Testov",
            isbn = "1234567891011"
        )
    
    def test_book_content(self):
        self.assertEqual(self.book.title, "Test Title")
        self.assertEqual(self.book.subtitle, "Exelent test subtitle")
        self.assertEqual(self.book.author, "Test Testov")
        self.assertEqual(self.book.isbn, "1234567891011")
    
class APITests(APITestCase):
    """Test cases for testing BOOK APIs"""

    @classmethod
    def setUpTestData(self):
        self.book = Book.objects.create(
            title = "Test Book Title",
            subtitle = "Exelent test subtitle",
            author = "Test Testov",
            isbn = "1234567891011"
        )
    
    def test_api_listview(self):
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 1)
        # self.assertContains(response, self.book)
