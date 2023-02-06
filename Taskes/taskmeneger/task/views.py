from django.shortcuts import render
from django.http import HttpRequest
from .models import task_db
# Create your views here.


def index(request):
    todos = task_db.objects.all()
    return render(request, 'todo.html', {'todo_list': todos, 'title': 'Главная страница'})

def singin(request):
    return render(request, 'singin.html')
def login(request):
    return render(request, 'login.html')

def important (request):
    return render (request, 'important.html')