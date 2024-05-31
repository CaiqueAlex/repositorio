from django.db import models
from django.contrib.auth.models import User

class Palavra(models.Model):
    palavra = models.CharField(max_length=5, unique=True)

    def __str__(self):
        return self.palavra