from django.db import models
from django.contrib.auth.models import User

class Word(models.Model):
    content = models.CharField(max_length=5, default='')

    def __str__(self):
        return self.content