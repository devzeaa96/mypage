from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('about/', views.about),
    path('services/', views.services),
    path('contact/', views.contact),
]