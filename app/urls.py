from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='loginPage'),
    path('singup/', views.login, name='singUpPage'),
    path('game/', views.game, name='game'),
]
