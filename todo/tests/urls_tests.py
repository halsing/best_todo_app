from django.test import SimpleTestCase
from django.urls import reverse, resolve

from todo.views import (
    index,
    TodoListView,
    TodoDetailView,
    TodoListCreateView,
    todo_add,
    todo_edit,
    todo_delete,
    todo_complete,
    todo_delete_completed,
    todo_delete_all,
)


class TestTodoUrls(SimpleTestCase):
    def test_home_url_resolves(self):
        url = reverse("todo:todo-home")
        self.assertEqual(resolve(url).func.view_class, TodoListView)

    def test_todo_list_detail_url_resolves(self):
        url = reverse("todo:todo-detail", args=[1])
        self.assertEqual(resolve(url).func.view_class, TodoDetailView)

    def test_create_todo_list_url_resolves(self):
        url = reverse("todo:create")
        self.assertEqual(resolve(url).func.view_class, TodoListCreateView)

    def test_edit_todo_url_resolves(self):
        url = reverse("todo:todo_edit", args=[1])
        self.assertEqual(resolve(url).func, todo_edit)

    def test_add_todo_url_resolves(self):
        url = reverse("todo:todo-add", args=[1])
        self.assertEqual(resolve(url).func, todo_add)

    def test_delete_todo_url_resolves(self):
        url = reverse("todo:todo-delete", args=[1])
        self.assertEqual(resolve(url).func, todo_delete)

    def test_delete_all_todo_url_resolves(self):
        url = reverse("todo:todo_delete_all", args=[1])
        self.assertEqual(resolve(url).func, todo_delete_all)

    def test_complete_todo_url_resolves(self):
        url = reverse("todo:todo-complete", args=[1])
        self.assertEqual(resolve(url).func, todo_complete)

    def test_delete_completed_todo_url_resolves(self):
        url = reverse("todo:todo_delete_completed", args=[1])
        self.assertEqual(resolve(url).func, todo_delete_completed)
