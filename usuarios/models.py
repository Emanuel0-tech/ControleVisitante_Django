from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, BaseUserManager)

<<<<<<< HEAD
=======
# Create your models here.
>>>>>>> 259bea34cf67988f3aafeb19514fc5d39454096e
class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None):
        usuario = self.model(
            email = self.normalize_email(email)
        )
        usuario.is_active = True
        usuario.is_staff = False
        usuario.is_superuser = False
<<<<<<< HEAD
        
        if password:
            usuario.set_password(password)
            
        usuario.save()
        return usuario
    
    def create_superuser(self, email, password):
        usuario = self.create_user(
            email = self.normalize_email(email),
            password= password,
=======

        if password:
            usuario.set_password(password)

        usuario.save()
        return usuario

    def create_superuser(self, email, password):
        usuario = self.create_user(
            email = self.normalize_email(email), password= password,
>>>>>>> 259bea34cf67988f3aafeb19514fc5d39454096e
        )
        usuario.is_active = True
        usuario.is_staff = True
        usuario.is_superuser = True
<<<<<<< HEAD
        
        if password:
            usuario.set_password(password)
            
        usuario.save()
        return usuario
    
    
class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='E-mail do usuário',max_length=200,unique=True)
    is_active = models.BooleanField(verbose_name='Usuário está ativo', default=True)
    is_staff = models.BooleanField(verbose_name='Usuário é da equipe de desenvolvimento', default=False)
    is_superuser = models.BooleanField(verbose_name='Usuário é um superusuario', default=False)
    
    USERNAME_FIELD = 'email'
    
    objects = UsuarioManager()
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'usuario'
        
=======

        if password:
            usuario.set_password(password)

        usuario.save()
        return usuario


class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='E-mail do usuário', max_length=200, unique=True)
    is_active = models.BooleanField(verbose_name='Usuário esta ativo', default=True)
    is_staff = models.BooleanField(verbose_name='Usuário é da equipe de desenvolvimento', default=False)
    is_superuser = models.BooleanField(verbose_name='Usuário é um superusuário', default=False)

    USERNAME_FIELD = 'email'

    objects = UsuarioManager()

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        db_table = 'usuário'

>>>>>>> 259bea34cf67988f3aafeb19514fc5d39454096e
    def __str__(self):
        return self.email