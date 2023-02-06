from django.db import models
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect

# Create your models here.


class task_db(models.Model):
    title = models.CharField('Название Задания', max_length=255)
    is_complete = models.BooleanField('Завершено', default=False)
    user = models.CharField('Имя', max_length=55, default='NoName')

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def __str__(self):
        return self.title

@require_http_methods(['POST'])
def add(request):
    title = request.POST['title']
    todo = task_db(title=title)
    todo.save()
    return redirect('index')

def update(request, todo_id):
    todo = task_db.objects.get(id=todo_id)
    todo.is_complete = not todo.is_complete
    todo.save()
    return redirect('index')

def delete(request, todo_id):
    todo = task_db.objects.get(id=todo_id)
    todo.delete()
    return redirect('index')