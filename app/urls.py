from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='loginPage'),
    # path('password/', views.password_reset_form, name='password_reset_form'),
    path('register/', views.register, name='registerPage'),
    path('game/', views.game, name='game'),
    path('salvar_dados/', views.salvar_dados, name='salvar_dados'),
    # path('password_reset/', views.MyPasswordReset.as_view(), name='password_reset'),
    # path('password_reset/done/', views.MyPasswordResetDone.as_view(), name='password_reset_done'),
    path('password_reset/', views.password_reset_request, name='password_reset'),  # URL de "Esqueci minha Senha"
    path('register/', views.register, name='register'),
]

