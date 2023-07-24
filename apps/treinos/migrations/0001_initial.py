# Generated by Django 4.2.2 on 2023-07-24 18:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercicios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='nome')),
                ('num_series', models.PositiveIntegerField(verbose_name='numero de series')),
                ('num_repeticoes', models.PositiveIntegerField(verbose_name='numero de repeticoes')),
                ('descanco', models.CharField(max_length=100, verbose_name='Tempo de descanço')),
                ('img', models.ImageField(blank=True, null=True, upload_to='exercicios/imagens', verbose_name='imagem descritiva')),
                ('video', models.CharField(blank=True, max_length=100, verbose_name='link do Video descritivo')),
                ('descricao', models.TextField(blank=True, verbose_name='Descricao')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='exercicios', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Treinos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='nome')),
                ('descricao', models.TextField(blank=True, verbose_name='Descricao')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='treinos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Exercicios_do_treino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercicio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='exercicio_do_treino', to='treinos.exercicios')),
                ('treino', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='exercicios_do_treino', to='treinos.treinos')),
            ],
        ),
    ]
