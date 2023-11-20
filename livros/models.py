from django.db import models
from datetime import datetime

class Meus_livros(models.Model):#Esta classe se transforma em uma tabela no banco de dados.
    meus_livros = models.TextField(max_length=255)
    resumo = models.TextField(max_length=255)
    lido = models.BooleanField(default=False)
    data_inicio = models.DateField(default=datetime.now)    
    data_termino = models.DateField(null=True, blank=True)    
    
# Create your models here.
