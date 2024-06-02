from django.shortcuts import render, redirect
import os
from django.conf import settings
from django.contrib import messages
from .forms import RegisterForm, LoginForm, ResetPasswordForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import Palavra
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, LogoutView
from django.contrib.auth.forms import PasswordResetForm, UserCreationForm, AuthenticationForm
from django.template.loader import get_template
import hashlib
import random

def register(request):
    if request.method == 'POST':
        print("Formulário POST recebido")
        form = RegisterForm(request.POST)
        if form.is_valid():
            print("Formulário é válido")
            user = form.save()
            login(request, user)
            messages.success(request, 'Conta criada com Sucesso!')
            return redirect('termo')  # Certifique-se que esta URL está correta
        else:
            print("Formulário não é válido")
            print(form.errors)
    else:
        form = RegisterForm()
    return render(request, 'registerPage.html', {'form': form})

def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, 'Logado com Sucesso!')
                return redirect('termo')
        else:
            return render(request, 'loginPage.html', {'form': form, 'error': 'Usuário ou senha incorretos.'})
    else:
        form = LoginForm()
        error = None
    return render(request, 'loginPage.html', {'form': form})

import os

import os

def salvar_dados(request):
    if request.method == 'POST':
        letra1 = request.POST.get('letra1', '').strip().lower()
        letra2 = request.POST.get('letra2', '').strip().lower()
        letra3 = request.POST.get('letra3', '').strip().lower()
        letra4 = request.POST.get('letra4', '').strip().lower()
        letra5 = request.POST.get('letra5', '').strip().lower()

        palavra = letra1 + letra2 + letra3 + letra4 + letra5

        if len(palavra) != 5:
            return JsonResponse({'erro': 'Digite 5 letras!'}, status=400)

        arquivo_palavras = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'js', 'arquivo_palavras.txt')

        if not os.path.exists(arquivo_palavras):
            return JsonResponse({'erro': 'Arquivo de palavras não encontrado!'})

        with open(arquivo_palavras, 'r') as file:
            palavras_validas = [linha.strip().lower() for linha in file]

        if palavra not in palavras_validas:
            return JsonResponse({'erro': 'Palavra inválida!'}, status=400)

        return JsonResponse({'mensagem': 'Dados salvos com sucesso!'})
    else:
        return JsonResponse({'erro': 'Método não permitido'}, status=405)




def password_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        try:
            user = User.objects.get(username=username)
            form = ResetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()  # Isso salva a nova senha no usuário
                messages.success(request, 'Senha redefinida com sucesso! Faça login com sua nova senha.')
                return redirect('login')  # Redireciona para a página de login
        except User.DoesNotExist:
            form = ResetPasswordForm(None, request.POST)  # Passamos None se o usuário não for encontrado
            return render(request, 'passwordPage.html', {'form': form, 'error': 'Usuário não encontrado.'})
    else:
        form = ResetPasswordForm(None)
    return render(request, 'passwordPage.html', {'form': form})

def index(request):
    return render(request, 'index.html')

@login_required(login_url='http://127.0.0.1:8000')
def termo(request):
    user_not_authenticated = not request.user.is_authenticated
    return render(request, 'loggedIndex.html', {'user_not_authenticated': user_not_authenticated})

@login_required(login_url='http://127.0.0.1:8000')
def game(request):
    palavra_aleatoria = Palavra.objects.order_by('?').first()
    user_not_authenticated = not request.user.is_authenticated
    return render(request, 'game.html', {'palavra_aleatoria': palavra_aleatoria, 'user_not_authenticated': user_not_authenticated})
