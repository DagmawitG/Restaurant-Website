from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='restaurant-home'),
    path('contact-us/', views.contact, name='contact-us'),
]
