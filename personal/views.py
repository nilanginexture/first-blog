from django.shortcuts import render

def index(request):
    return render(request, 'personal/home.html')

def index(request):
    return render(request, 'personal/index.html')

def contact(request):
    return render(request, 'personal/basic.html',{'content':['Contact me at :','nilangprajapati@gmail.com']})
