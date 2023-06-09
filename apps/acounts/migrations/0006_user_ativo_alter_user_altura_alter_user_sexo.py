# Generated by Django 4.2.2 on 2023-07-02 21:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acounts', '0005_alter_user_altura_alter_user_peso'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ativo',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='altura',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(2)], verbose_name='Altura'),
        ),
        migrations.AlterField(
            model_name='user',
            name='sexo',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Sexo'),
        ),
    ]
