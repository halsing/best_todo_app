from django.test import TestCase
from django.contrib.auth.models import User

from todo.models import TodoList, Todo


class TestTodoListModels(TestCase):

    def setUp(self):
        self.user_test = User.objects.create_user(
            username="Test1", password="asdasdasd12312", email='asda@o2.pl')

        self.todo_list = TodoList.objects.create(
            name='test 1',
            author=self.user_test,
        )

    def test_todo_list_created(self):
        self.assertEqual(self.todo_list.name, 'test 1')
        self.assertEqual(self.todo_list.author.username, "Test1")

    def test_todo_list_author_photo(self):
        self.assertEqual(
            self.todo_list.author.profile.image, "profile_image/default.jpg")


class TestTodoModels(TestCase):

    def setUp(self):
        self.user_test = User.objects.create_user(
            username="Test1", password="asdasdasd12312", email='asda@o2.pl')

        self.todo_list = TodoList.objects.create(
            name='test 1',
            author=self.user_test,
        )

    def test_todo_create(self):
        my_text = "test thing"
        todo = Todo.objects.create(
            text=my_text,
            todo_list=self.todo_list,
        )

        self.assertEqual(todo.text, my_text)
        self.assertEqual(todo.complete, False)
        self.assertEqual(todo.todo_list.name, 'test 1')
