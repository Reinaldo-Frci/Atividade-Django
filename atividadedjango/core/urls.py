from django.urls import path
from .views import *


urlpatterns = [
    path('', homepage),
    path('jogo/', jogo_adivinhacao, name='jogo'),
]
