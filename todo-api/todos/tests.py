from django.test import TestCase

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