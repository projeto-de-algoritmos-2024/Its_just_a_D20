# knapsack_app/urls.py
from django.urls import path
from . import views




urlpatterns = [
    path('', views.knapsack_view, name='knapsack'),
    path('resultado/', views.resultado_view, name='resultado'),
]
