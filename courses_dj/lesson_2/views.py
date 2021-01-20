from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View

# Create your views here.

def starter(request, username):
    return HttpResponse(f'<h1>{username}</h1> ')
    #return HttpResponseRedirect('/') #редирект на главную страницу


class MyView(View):
    def get(self, request, username):
        return HttpResponse(f'Добро пожаловать на третий урок, {username}')