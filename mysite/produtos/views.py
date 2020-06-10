from django.shortcuts import render
from .models import Produto


def home(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos.html', {'produtos': produtos})


def novo(request):
    return render(request, 'novo.html')
