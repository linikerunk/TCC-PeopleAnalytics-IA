# Generated by Django 2.2 on 2020-08-20 02:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200818_2325'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='costcenter',
            options={'verbose_name': 'Centro de Custo', 'verbose_name_plural': 'Centro de Custos'},
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name': 'Funcionário', 'verbose_name_plural': 'Funcionários'},
        ),
        migrations.AlterModelOptions(
            name='unity',
            options={'verbose_name': 'Unidade', 'verbose_name_plural': 'Unidades'},
        ),
    ]
