from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView
from django.contrib.auth.forms import PasswordResetForm, UserCreationForm, AuthenticationForm
from django.template.loader import get_template
import hashlib

def register(request):
    if request.method == 'POST':
        print("Formulário POST recebido")
        form = RegisterForm(request.POST)
        if form.is_valid():
            print("Formulário é válido")
            user = form.save()
            login(request, user)
            return redirect('game')  # Certifique-se que esta URL está correta
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
            # password_hashed = hashlib.md5(password.encode()).hexdigest()
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('game')  # Redirecionar para a página do jogo após login bem-sucedido
        else:
            return render(request, 'loginPage.html', {'form': form, 'error': 'Usuário ou senha incorretos.'})
    else:
        form = LoginForm()
        error = None
    return render(request, 'loginPage.html', {'form': form})

# def password_reset_request(request):
#     if request.method == 'POST':
#         form = PasswordResetForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request, 'password_reset_done.html')
#     else:
#         form = PasswordResetForm()
#     return render(request, 'password_reset_form.html', {'form': form})

def index(request):
    return render(request, 'index.html')

def game(request):
    return render(request, 'game.html')

# class MyPasswordReset(PasswordResetView):
#     '''
#     Requer
#     registration/password_reset_form.html
#     registration/password_reset_email.html
#     registration/password_reset_subject.txt 
#     '''
#     ...

# class MyPasswordResetDone(PasswordResetDoneView):
#     '''
#     Requer
#     registration/password_reset_done.html
#     '''
#     ...

def salvar_dados(request):
    if request.method == 'POST':
        # Recebe os dados dos inputs via POST
        dados = request.POST

        # Aqui você pode processar os dados recebidos e salvá-los no banco de dados
        # Por exemplo, supondo que você tenha um modelo chamado Dados:
        # from minhaapp.models import Dados
        # Dados.objects.create(campo1=dados['campo1'], campo2=dados['campo2'], ...)

        return JsonResponse({'mensagem': 'Dados salvos com sucesso!'})

    return JsonResponse({'erro': 'Método não permitido'}, status=405)
