from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Post
# Create your tests here.
class BlogTests(TestCase):
    """Test cases for blog posts"""
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create(
            username = "testuser",
            email = "test@example.com",
            password = "secrettest"
        )

        cls.post = Post.objects.create(
            author = cls.user,
            title = "The best test title",
            body = "Exelent test body content"
        )
    
    def test_post_model(self):
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(self.post.title, "The best test title")
        self.assertEqual(self.post.body, "Exelent test body content")
        self.assertEqual(str(self.post), "The best test title")