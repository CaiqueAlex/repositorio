from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, SetPasswordForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Usuário')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)

class ResetPasswordForm(SetPasswordForm):
    username = forms.CharField(max_length=150, label='Nome de Usuário')

    def __init__(self, user, *args, **kwargs):
        super(ResetPasswordForm, self).__init__(user, *args, **kwargs)
        self.fields['new_password1'].label = 'Nova Senha'
        self.fields['new_password2'].label = 'Confirme sua Senha'