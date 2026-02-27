from django.urls import path
from . import views

urlpatterns = [
    path('health/',views.health),
    path('homepage/',views.homepage,name='homepage'),
    path('homepage/about/',views.about,name='about')
]