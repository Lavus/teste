# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cloudinary.models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20170928_1853'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ExampleModel',
        ),
        migrations.AlterField(
            model_name='depoimento',
            name='imagem',
            field=cloudinary.models.CloudinaryField(max_length=255, default=datetime.datetime(2017, 9, 30, 13, 54, 1, 740234, tzinfo=utc), verbose_name='imagem'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='destaque',
            name='imagem',
            field=cloudinary.models.CloudinaryField(max_length=255, default=datetime.datetime(2017, 9, 30, 13, 54, 6, 673828, tzinfo=utc), verbose_name='imagem'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='imagem',
            name='imagem',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='imagem'),
        ),
    ]
