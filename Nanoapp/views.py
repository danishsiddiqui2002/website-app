from multiprocessing import context
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
  return render(request,'index.html')

def services(request):
  return render(request,'services.html')
def service1(request):
  return render(request,'service1.html')
def service2(request):
  return render(request,'service2.html')
def service3(request):
  return render(request,'service3.html')
def service4(request):
  return render(request,'service4.html')
def service5(request):
  return render(request,'service5.html')
def service6(request):
  return render(request,'service6.html')
def service7(request):
  return render(request,'service7.html')
def service8(request):
  return render(request,'service8.html')
def service9(request):
  return render(request,'service9.html')
  
def lms(request):
  return render(request,'lms.html')

def blog(request):
  return render(request,'blog.html')

def contact(request):
  return render(request,'contact.html')

def about(request):
  return render(request,'about.html')

def announcement(request):
  return render(request,'announcement.html')  