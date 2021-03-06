# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-10 00:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compromisso', models.DateField(blank=True, null=True)),
                ('descricao', models.TextField()),
                ('privado', models.BooleanField()),
                ('institucional', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Convite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=128)),
                ('compromisso', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='compromissoUsuarioConvidado', to='agenda.Agenda')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iduser', models.CharField(max_length=128)),
                ('nome', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioAgenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compromisso', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='compromissoUsuario', to='agenda.Agenda')),
                ('convidados', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='agenda.Convite')),
                ('nome', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='NomeUsuario', to='agenda.Usuario')),
            ],
        ),
        migrations.AddField(
            model_name='convite',
            name='nome',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='NomeUsuarioConvidado', to='agenda.Usuario'),
        ),
        migrations.AddField(
            model_name='agenda',
            name='iduser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='agenda.Usuario'),
        ),
    ]
