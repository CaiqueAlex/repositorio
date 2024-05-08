from django.contrib import admin

from .models import word, Player

@admin.register(word)
class wordAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Informações Basicas',           {'fields': ('nome', 'nivel', 'tamanho' )}),
    ]

    list_display = ('nome', 'nivel', 'tamanho',)

    search_fields = ['nome']

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):


    fieldsets = [
        ("Informações do Usuario",           {'fields': ('usuario', 'senha')})
    ]

    list_display = ('usuario', 'senha')