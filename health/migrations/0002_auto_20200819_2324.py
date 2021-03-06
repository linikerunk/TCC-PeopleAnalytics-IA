# Generated by Django 2.2 on 2020-08-20 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bodymassindex',
            name='classification_text',
            field=models.CharField(choices=[('Magreza grave', 'Magreza grave'), ('Magreza moderada', 'Magreza moderada'), ('Magreza leve', 'Magreza leve'), ('Saudável', 'Saudável'), ('Sobrepeso', 'Sobrepeso'), ('Obesidade Grau I', 'Obesidade Grau I'), ('Obesidade Grau II (severa)', 'Obesidade Grau II (severa)'), ('Obesidade Grau III (mórbida)', 'Obesidade Grau III (mórbida)')], max_length=28, null=True, verbose_name='Classificação IMC'),
        ),
        migrations.AlterField(
            model_name='bodymassindex',
            name='imc',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='IMC'),
        ),
    ]
