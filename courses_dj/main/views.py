from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

data = {
    'title': 'Главная страница',
    'values': ['Some', 'text', '123']
    }


def index(request):
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')
