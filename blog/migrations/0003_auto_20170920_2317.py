# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-21 02:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170919_1947'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={},
        ),
        migrations.AlterModelOptions(
            name='imagem',
            options={},
        ),
        migrations.RemoveField(
            model_name='album',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='imagem',
            name='descricao',
        ),
        migrations.RemoveField(
            model_name='imagem',
            name='published_date',
        ),
        migrations.RemoveField(
            model_name='imagem',
            name='slug',
        ),
        migrations.AddField(
            model_name='imagem',
            name='imagem',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
