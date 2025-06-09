from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=25)
    cpf = models.CharField(max_length=14, unique=True)
    OPCOES_SEXO = {
        "M": "Masculino",
        "F": "Feminino",
        "O": "Outro"      
    }
    sexo = models.CharField(max_length=1, choices=OPCOES_SEXO)
    data_nasc = models.DateField()

    def __str__(self):
        return self.nome