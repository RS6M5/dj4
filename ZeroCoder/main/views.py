from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def new(request):
    return HttpResponse ("<h1>Это вторая страница моего проекта на Django</h1>")