from django.contrib import admin

from .models import word, Player

@admin.register(word)
class wordAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Informações Basicas',           {'fields': ('nome', 'nivel', 'tamanho' )}),
    ]

    list_display = ('nome', 'nivel', 'tamanho',)

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):

    list_display = ('senha', 'usuario')

    fieldsets = [
        ("Informações do Usuario",           {'fields': ('senha', 'usuario')})
    ]