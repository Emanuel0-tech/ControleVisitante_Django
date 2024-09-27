# Generated by Django 5.1.1 on 2024-09-27 20:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('porteiros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('AGUARDANDO', 'Aguardando Autorização'), ('EM_VISITA', 'Em Visita'), ('FINALIZADO', 'Visita Finalizada')], default='AGUARDANDO', max_length=10, verbose_name='status')),
                ('nome_completo', models.CharField(max_length=200, verbose_name='Nome completo')),
                ('cpf', models.CharField(max_length=11, verbose_name='CPF')),
                ('telefone', models.CharField(max_length=11, verbose_name='Telefone')),
                ('data_nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('numero_casa', models.PositiveSmallIntegerField(verbose_name='Número da casa a ser visitada')),
                ('placa_veiculo', models.CharField(blank=True, max_length=7, null=True, verbose_name='Placa do Carro')),
                ('horario_chegada', models.DateTimeField(auto_now_add=True, verbose_name='Horario de chegada na portaria')),
                ('horario_autorizacao', models.DateTimeField(blank=True, null=True, verbose_name='Horario da autorização de entrada')),
                ('horario_saida', models.DateTimeField(blank=True, null=True, verbose_name='Horario de saida do condominio')),
                ('morador_responsavel', models.CharField(max_length=200, verbose_name='Nome do morador responsavel')),
                ('registrado_por', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='porteiros.porteiro', verbose_name='Porteiro responsavel pelo registro')),
            ],
            options={
                'verbose_name': 'Visitante',
                'verbose_name_plural': 'Visitantes',
                'db_table': 'visitante',
            },
        ),
    ]
