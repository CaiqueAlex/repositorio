from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView
from django.contrib.auth.forms import PasswordResetForm, UserCreationForm
from django.template.loader import get_template


def password_reset_request(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'password_reset_done.html')
    else:
        form = PasswordResetForm()
    return render(request, 'password_reset_form.html', {'form': form})

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'loginPage.html')

def register(request):
    return render(request, 'registerPage.html')

def game(request):
    return render(request, 'game.html')


class MyPasswordReset(PasswordResetView):
    '''
    Requer
    registration/password_reset_form.html
    registration/password_reset_email.html
    registration/password_reset_subject.txt 
    '''
    ...


class MyPasswordResetDone(PasswordResetDoneView):
    '''
    Requer
    registration/password_reset_done.html
    '''
    ...

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

def register(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      # Redirecionar para página de sucesso (opcional)
      # return redirect('pagina_sucesso')
      return render(request, 'registration_success.html')  # Exemplo de página de sucesso
  else:
    form = UserCreationForm()
  return render(request, 'registerPage.html', {'form': form})
