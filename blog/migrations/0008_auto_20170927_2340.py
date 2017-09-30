# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20170927_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagem',
            name='album',
            field=models.ForeignKey(related_name='imagens', to='blog.Imovel'),
        ),
    ]
