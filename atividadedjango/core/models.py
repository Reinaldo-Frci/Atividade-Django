from django.db import models

# Create your models here.

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    data_nascimento = models.DateField()
    matriculado = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
