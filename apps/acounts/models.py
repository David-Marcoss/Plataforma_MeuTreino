from django.db import models
from django.contrib.auth.models import AbstractUser

from django.conf import settings
from Meu_Treino.settings import AUTH_USER_MODEL

# Create your models here.


class User(AbstractUser):
    
    nome = models.CharField('Nome completo',max_length=100,null=True,blank=True)
    imageperfil = models.ImageField(upload_to='perfil/imagens',verbose_name='imagem perfil',null=True,blank=True)
    email = models.EmailField('E-mail',blank=False,unique=True)
    nascimento = models.DateField("Data de Nascimento",null=True,blank=True)
    sexo = models.CharField('Nome completo',max_length=100,null=True,blank=True)
    peso = models.DecimalField("Altura",max_digits=4,decimal_places=2,null=True,blank=True)
    altura = models.DecimalField("Altura",max_digits=2,decimal_places=2,null=True,blank=True)

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        db_table = "usuario"

    def __str__(self):
        return f"{self.username}"



"""
    Este model serve para auxiliar na recuperação de senhas do usuario
    e armazenar o historico de auterações de senha ele aramzenha o ususario
    que esta tenteando alterar senha, uma chave unica string para gerar um link
    para que o usuario possa alterar senha e a data da criação da geração da chave
    e se uma confirmação para que seja indicado se a senha foi ou nao alterada 

"""
class redefinir_senha(models.Model):

    User = models.ForeignKey(User,verbose_name='Usuario', related_name='resets',on_delete=models.PROTECT)
    key = models.TextField('key',max_length=100,unique=True)
    criado_em = models.DateField('Data criação',auto_now=True)
    confirmado = models.BooleanField('Senha foi redefinida:',default=False)
    horario = models.TimeField('horario de criação',auto_now=True)
    expira_em = models.TimeField('tempo para expirar',null=True)

    def __str__(self):
        return f"{self.User} {self.criado_em}"
    
    class meta:
        verbose_name = 'Nova senha'
        verbose_name_plural = 'Novas senhas'
        ordering = ['-criado_em']



