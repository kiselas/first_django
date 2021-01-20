
from django.urls import path
from . import views

urlpatterns = [
    path('starter/<username>/', views.MyView.as_view(), name='starter'),
]