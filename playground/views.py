from django.shortcuts import render
from django.http import HttpResponse

# NOTE: This is a request handler

# Create your views here.

def say_hello(request):
    return render(request, 'hello.html', {'name' : 'Davit'})
