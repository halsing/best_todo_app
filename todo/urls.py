from django.urls import path
from . import views

app_name = "todo"

urlpatterns = [
    # path('', views.index , name="todo-home"),
    path("", views.TodoListView.as_view(), name="todo-home"),
    path("todo/<int:pk>", views.TodoDetailView.as_view(), name="todo-detail"),
    path("new/", views.TodoListCreateView.as_view(), name="create"),
    path("edit_todo/<int:todolist_pk>", views.todo_edit, name="todo_edit"),
    path("add_todo/<int:todolist_pk>", views.todo_add, name="todo-add"),
    path("delete_todo/<int:todo_pk>", views.todo_delete, name="todo-delete"),
    path(
        "delete_all_todo/<int:todolist_pk>",
        views.todo_delete_all,
        name="todo_delete_all",
    ),
    path("complete_todo/<int:todo_pk>", views.todo_complete, name="todo-complete"),
    path(
        "delete_completed_todo/<int:todolist_pk>",
        views.todo_delete_completed,
        name="todo_delete_completed",
    ),
]
