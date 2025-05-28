from ast import Import
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from app.models import Todo

# Create your views here.
def home (request):
  return render(request,'home.html')
def add (request):
  if request.method == 'POST':
    title = request.POST.get('title')
    desc = request.POST.get('desc')
    todo = Todo(title=title, desc=desc)
    todo.save()
    return HttpResponseRedirect(reverse('list'))
  return render(request, 'add.html')

def list (request):
    all_todos = Todo.objects.all()
    return render(request, 'list.html',{'all_todos': all_todos})
 