<<<<<<< HEAD
# Generated by Django 5.1.1 on 2024-09-26 19:12

import django.db.models.deletion
from django.conf import settings
=======
# Generated by Django 5.1.1 on 2024-09-26 19:14

>>>>>>> 259bea34cf67988f3aafeb19514fc5d39454096e
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
<<<<<<< HEAD
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
=======
>>>>>>> 259bea34cf67988f3aafeb19514fc5d39454096e
    ]

    operations = [
        migrations.CreateModel(
            name='Porteiro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=200, verbose_name='Nome Completo')),
                ('cpf', models.CharField(max_length=11, verbose_name='CPF')),
<<<<<<< HEAD
                ('telefone', models.CharField(max_length=11, verbose_name='Telefone de Contato')),
                ('data_nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Porteiro',
                'verbose_name_plural': 'Porteiros',
                'db_table': 'porteiro',
            },
=======
                ('telefone', models.CharField(max_length=11, verbose_name='Telefone de contato')),
                ('data_nascimento', models.DateField(verbose_name='Data de Nascimento')),
            ],
>>>>>>> 259bea34cf67988f3aafeb19514fc5d39454096e
        ),
    ]
