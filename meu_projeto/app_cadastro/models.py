from django.db import models
from django.db import models

# Create your models here

def __str__(self):
        return self.nome  
    
from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    endereco = models.TextField()

    def __str__(self):
        return self.nome
    
    
