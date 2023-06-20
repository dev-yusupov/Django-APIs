from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from .models import Todo #importing Todo model

# Create your tests here.
class TestTodoModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(
            title="Test Todo",
            body="Test body of todo"
        )
    
    def test_todo_content(self):
        self.assertEqual(self.todo.title, "Test Todo")
        self.assertEqual(self.todo.body, "Test body of todo")
        self.assertEqual(str(self.todo), "Test Todo")

    def test_api_listview(self):
        response = self.client.get(reverse("todo_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, self.todo)
    
    def test_api_detail(self):
        response = self.client.get(
            reverse("todo_detail", kwargs={"pk": self.todo.id}),
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, "Test Todo")