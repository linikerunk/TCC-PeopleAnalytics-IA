# Generated by Django 2.2 on 2020-08-20 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0006_instructor_training'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entity',
            name='phone',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='Telefone'),
        ),
    ]
