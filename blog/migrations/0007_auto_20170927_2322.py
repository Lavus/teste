# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_imagem_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagem',
            name='album',
            field=models.ForeignKey(to='blog.Imovel', related_name='images'),
        ),
    ]
