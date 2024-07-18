from django.db import models
from datetime import datetime


# Create your models here.
class Tabela(models.Model):
    

    fase = models.CharField(max_length=100, null=True, blank=True, default='novo')
    descricao = models.CharField(max_length=255, null=True, blank=True, default='novo')
    responsavel = models.CharField(max_length=20, null=True, blank=True, default='novo')
    inicio_data = models.DateField(default=datetime.now, null=True, blank=True )
    fim_data = models.DateField(default=datetime.now, null=True, blank=True )
    status = models.CharField(max_length=10, null=True, blank=True, default='novo')
    projeto = models.CharField(max_length=20, default='Projeto')
    
    
    
    def __str__(self) -> str:
        return self.name


#    def __str__(self):
#        return "{} ({})".format(self.fase, self.descricao, self.campo.nome)
