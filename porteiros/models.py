from django.db import models

<<<<<<< HEAD
class Porteiro(models.Model):
    usuario = models.OneToOneField('usuarios.Usuario',verbose_name= 'Usuário', on_delete=models.PROTECT)
    nome_completo = models.CharField(verbose_name="Nome Completo", max_length=200)
    cpf = models.CharField(verbose_name='CPF', max_length=11)
    telefone = models.CharField(verbose_name='Telefone de Contato', max_length=11)
    data_nascimento = models.DateField(verbose_name='Data de Nascimento',auto_now=False, auto_now_add=False)
    
    class Meta:
        verbose_name = "Porteiro"
        verbose_name_plural = "Porteiros"
        db_table = "porteiro"
    
    def __str__(self) -> str:
        return self.nome_completo
        
       
=======
# Create your models here.

class Porteiro(models.Model):
    usuario = models.OneToOneField('usuarios.Usuario', verbose_name='Usuário', on_delete=models.PROTECT)
    nome_completo = models.CharField(verbose_name='Nome Completo', max_length=200)
    cpf = models.CharField(verbose_name='CPF', max_length=11)
    telefone = models.CharField(verbose_name='Telefone de contato', max_length=11)
    data_nascimento = models.DateField(verbose_name='Data de Nascimento', auto_now=False, auto_now_add=False)

class Meta:
    verbose_name = "Porteiro"
    verbose_name_plural = "Porteiros"
    db_table = "porteiro"

def __str__(self) -> str:
    return self.nome_completo
>>>>>>> 259bea34cf67988f3aafeb19514fc5d39454096e
