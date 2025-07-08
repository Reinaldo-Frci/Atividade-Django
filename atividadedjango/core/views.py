from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def homepage(request):
    return render(request, 'index.html')

def jogo_adivinhacao(request):
    mensagem = ''
    numero_secreto = 85  # número fixo para facilitar no início

    if request.method == 'POST':
        tentativa = int(request.POST.get('tentativa'))
        if tentativa == numero_secreto:
            mensagem = 'Parabéns! Você acertou!'
        elif tentativa > numero_secreto:
            mensagem = 'Tente um número menor.'
        else:
            mensagem = 'Tente um número maior.'

    return render(request, 'jogo.html', {'mensagem': mensagem})
