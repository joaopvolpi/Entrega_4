from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Postagem(models.Model):

    created_by =  models.ForeignKey(User,on_delete=models.CASCADE)
    nome = models.TextField()
    descricao = models.TextField()
    data_criada = models.DateTimeField(default=timezone.now)
    #imagem = models.ImageField()
    

def __str__(self):
    return self.nome