from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_page, name='login'),
    path('game/', views.game, name='game'),
    path('salvar_dados/', views.salvar_dados, name='salvar_dados'),
    # path('password_reset/', views.password_reset_request, name='password_reset'),
    path('register/', views.register, name='register'),
    path('termo/', views.termo, name='termo'),
    path('logout/', LogoutView.as_view(), name='logout'),
]