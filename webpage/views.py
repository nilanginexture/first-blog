from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    reture HttpResponse("<h1>WEL COME</h1>")
