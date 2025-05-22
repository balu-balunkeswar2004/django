from audioop import reverse
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from app.models import *
# Create your views here.
def home(request):
  return render (request,'home.html')
def register(request):
  if request.method == 'POST':
    empid = request.POST.get('userid')
    ename = request.POST.get('username')
    password = request.POST.get('password')
    pno = request.POST.get('pno')
    email = request.POST.get('email')
    add = request.POST.get('address')
    gender = request.POST.get('gender')
    EO = Employee(empid = empid,ename = ename,password = password,pno = pno,email = email,add = add,gender = gender)
    EO.save()
    return HttpResponseRedirect(reverse('login'))
  return render(request,'register.html')
def login(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    all_users = Employee.objects.all()
    for user in all_users:
      if user.ename == username:
        if user.password == password:
          return HttpResponse('login successfully')
        else:
          return HttpResponse('invalid pasword')
    else:
      return HttpResponse('invalid user')
  return render(request,'login.html')
 