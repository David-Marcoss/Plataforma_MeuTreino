from django.db import models
from apps.acounts.models import User

class Receitas(models.Model):
    nome = models.CharField('Nome',max_length=100)
    ingredientes = models.TextField("Ingredientes")
    preparo = models.TextField("Preparo")
    tempo_preparo = models.CharField("Tempo de Preparo",max_length=100)
    calorias = models.PositiveIntegerField("Calorias")
    img = models.ImageField(upload_to='exercicios/imagens',verbose_name='imagem descritiva',null=True,blank=True)
    video = models.CharField('link do Video descritivo',max_length=100,blank=True)
    user = models.ForeignKey(User,on_delete=models.PROTECT,related_name='receitas')
    categoria = models.CharField("Categoria",max_length=100,blank=False)
    criado_em= models.DateTimeField('criado em: ',auto_now_add=True)
    atualizado_em= models.DateTimeField('atualizado em: ',auto_now=True)


    def __str__(self):
        return self.nome
