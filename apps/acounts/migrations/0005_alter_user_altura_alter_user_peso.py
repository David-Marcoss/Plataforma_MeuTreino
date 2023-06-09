# Generated by Django 4.0.4 on 2023-06-30 20:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acounts', '0004_alter_user_altura_alter_user_nascimento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='altura',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=2, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(2)], verbose_name='Altura'),
        ),
        migrations.AlterField(
            model_name='user',
            name='peso',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(200)], verbose_name='Peso'),
        ),
    ]
