from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class TodoList(models.Model):
    name = models.CharField(max_length=80)
    created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("todo:todo-detail", kwargs={"pk": self.pk})


class Todo(models.Model):
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    start = models.DateTimeField(default=timezone.now)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.text
