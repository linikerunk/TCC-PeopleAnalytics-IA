# Generated by Django 3.1 on 2020-08-19 01:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modified', models.DateField(auto_now_add=True, verbose_name='Atualização')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('entity_name', models.CharField(max_length=100, verbose_name='Nome da Entidade')),
                ('social_reason', models.CharField(max_length=100, verbose_name='Razão Social')),
                ('cnpj', models.CharField(max_length=100, verbose_name='CNPJ')),
                ('sap_code', models.CharField(max_length=100, verbose_name='Código SAP')),
                ('contact_person', models.CharField(max_length=30, verbose_name='Pessoa Responsável')),
                ('phone', models.PositiveIntegerField(blank=True, null=True, verbose_name='Telefone')),
                ('zip_code', models.CharField(max_length=10, verbose_name='CEP')),
                ('address', models.CharField(max_length=60, verbose_name='Endereço')),
                ('city', models.CharField(max_length=50, verbose_name='Cidade')),
                ('state', models.CharField(default='XX', max_length=2, verbose_name='Estado')),
                ('email', models.EmailField(error_messages={'required': 'Porfavor digite seu e-mail.', 'unique': 'Já existe esse e-mail cadastrado.'}, max_length=70, unique=True, verbose_name='Email')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=80, verbose_name='Nome do Evento')),
                ('value', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Valor')),
                ('event_date', models.DateTimeField(blank=True, verbose_name='Data Consulta')),
                ('present_list', models.FileField(default='', upload_to='present_list', verbose_name='Lista de Presença')),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('created', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modified', models.DateField(auto_now_add=True, verbose_name='Atualização')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('registro_instrutor', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(9999999999), django.core.validators.MinValueValidator(0)], verbose_name='Registro Instrutor')),
                ('instructor_name', models.CharField(max_length=100, verbose_name='Nome Instrutor')),
                ('instructor_photo', models.ImageField(blank=True, null=True, upload_to='photos_instructor', verbose_name='Foto do Instrutor')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modified', models.DateField(auto_now_add=True, verbose_name='Atualização')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('training_name', models.CharField(max_length=100, verbose_name='Nome Treinamento')),
                ('category', models.CharField(max_length=25, verbose_name='Categoria')),
                ('content', models.TextField(verbose_name='Conteúdo')),
                ('required', models.CharField(max_length=50, verbose_name='Requisito')),
                ('resource', models.CharField(max_length=50, verbose_name='Recursos')),
                ('training_type', models.CharField(max_length=50, verbose_name='Tipo de Treinamento')),
                ('local', models.CharField(max_length=50, verbose_name='Local')),
                ('workload', models.IntegerField(verbose_name='Carga Horária')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
