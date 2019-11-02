from django.db import models
from django.utils import timezone
#from django.views.generic.dates import *

from django.contrib.auth.models import User

#A evolucao consiste do valor produzido pelo funcionario x 

class Evolucao(models.Model):
    
    valor_produzido = models.IntegerField()
    
    funcionario =  models.ForeignKey(User,on_delete=models.CASCADE)

    data_criada = models.DateField() #FORMATO DA DATA: "YYYY-MM-DD"
