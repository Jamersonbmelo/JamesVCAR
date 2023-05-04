# Generated by Django 4.1.7 on 2023-03-07 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=100, verbose_name='Placa')),
                ('marca', models.CharField(max_length=100, verbose_name='Marca')),
                ('modelo', models.CharField(max_length=100, verbose_name='Modelo')),
                ('comprar', models.DateField(verbose_name='Data de compra')),
                ('ano', models.CharField(max_length=10, verbose_name='Ano')),
            ],
            options={
                'verbose_name': 'carro',
                'verbose_name_plural': 'carros',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250, verbose_name='Nome')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('cpf', models.CharField(max_length=15, verbose_name='CPF')),
                ('data_nascimento', models.DateField(verbose_name='Data de nascimento')),
            ],
            options={
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Aluguel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=100, verbose_name='Codigo')),
                ('data_aluguel', models.DateField(verbose_name='Data de aluguel')),
                ('data_devolucao', models.DateField(verbose_name='Data de devolução')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor')),
                ('devolucao', models.BooleanField(verbose_name='Devolvido')),
                ('carro', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='carro_alugueis', to='aluguel.carro', verbose_name='carros')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='cliente_alugueis', to='aluguel.cliente', verbose_name='Cliente')),
            ],
            options={
                'verbose_name': 'Aluguel',
                'verbose_name_plural': 'Alugueis',
            },
        ),
    ]
