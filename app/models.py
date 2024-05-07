from django.db import models
from django.contrib import admin
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

class word(models.Model):

    FACIL = 'FACIL'
    MEDIO = 'MEDIO'
    DIFICIL = 'DIFICIL'
    
    escolha_nivel = [
        (FACIL, 'FACIL'),
        (MEDIO, 'MEDIO'),
        (DIFICIL, 'DIFICIL')
    ]

    GRANDE = 'GRANDE'
    MEDIO = 'MEDIO'
    PEQUENA = 'PEQUENA'

    escolha_tamanho = [
        (GRANDE, 'GRANDE'),
        (MEDIO, 'MEDIO'),
        (PEQUENA, 'PEQUENA')
    ]

    nome = models.CharField(max_length=30)
    nivel = models.CharField(max_length=20, choices=escolha_nivel, default='FACIL')
    tamanho = models.CharField(max_length=20, choices=escolha_tamanho, default='GRANDE')

    def __str__(self):
        return self.nome

class Player(models.Model):
    senha = models.CharField(max_length=25, unique=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.usuario.first_name