from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'loginPage.html')


def game(request):
    return render(request, 'game.html')