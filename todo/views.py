from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib import messages

from .forms import TodoForm
from .models import TodoList, Todo


# Create your views here.


def index(request):
    todo_list = TodoList.objects.all()
    context = {
        "todo_list": todo_list,
    }
    return render(request, "todo/index.html", context)


class TodoListView(ListView):
    model = TodoList
    template_name = "todo/index.html"
    context_object_name = "todo_list"
    ordering = ["-created"]


class TodoDetailView(DetailView):
    model = TodoList


class TodoListCreateView(CreateView):
    model = TodoList
    fields = [
        "name",
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("todo:todo_edit", kwargs={"todolist_pk": self.object.pk})


@require_POST
@login_required
def todo_add(request, todolist_pk):
    todolist = TodoList.objects.get(pk=todolist_pk)
    form = TodoForm(request.POST)

    if todolist.author == request.user:
        if form.is_valid():
            new_todo = Todo(text=request.POST["text"], todo_list=todolist,)
            new_todo.save()

    return redirect(f"/edit_todo/{todolist_pk}")


@login_required
def todo_edit(request, todolist_pk):
    todolist = TodoList.objects.get(pk=todolist_pk)
    todo_form = TodoForm
    context = {
        "todo_list": todolist,
        "form": todo_form,
    }
    return render(request, "todo/edit.html", context)


@login_required
def todo_delete(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    todo_list_pk = todo.todo_list.pk

    if todo.todo_list.author == request.user:
        todo.delete()

    return redirect(f"/edit_todo/{todo_list_pk}")


@login_required
def todo_complete(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    todo_list_pk = todo.todo_list.pk

    if todo.todo_list.author == request.user:
        if todo.complete is True:
            todo.complete = False

        else:
            todo.complete = True
        todo.save()

    return redirect(f"/edit_todo/{todo_list_pk}")


@login_required
def todo_delete_completed(request, todolist_pk):
    todolist = TodoList.objects.get(pk=todolist_pk)
    todolist_completed = todolist.todo_set.filter(complete__exact=True)

    if todolist.author == request.user:
        todolist_completed.delete()

    return redirect(f"/edit_todo/{todolist_pk}")


@login_required
def todo_delete_all(request, todolist_pk):
    todolist = TodoList.objects.get(pk=todolist_pk)

    if todolist.author == request.user:
        messages.success(
            request, f'Twoja lista o tytule "{todolist.name}" została usunięta!'
        )
        todolist.delete()
    return redirect("todo:todo-home")
