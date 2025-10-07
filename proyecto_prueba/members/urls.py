from django.urls import path
from . import views

urlpatterns = [
    path('claudio/', views.prueba),
]