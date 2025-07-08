from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def homepage(request):
    return render(request, 'index.html')

def jogo_adivinhacao(request):
    mensagem = ''
    request.session['numero_secreto'] = random.randint(0, 100)
    numero = request.session['numero_secreto']
    if request.method == 'POST':
        tentativa = int(request.POST.get('tentativa'))
        if tentativa == numero:
            mensagem = 'Parabéns! Você acertou!'
        elif tentativa > numero:
            mensagem = 'Tente um número menor.'
        else:
            mensagem = 'Tente um número maior.'

    return render(request, 'jogo.html', {'mensagem': mensagem})
