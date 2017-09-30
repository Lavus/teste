# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170921_0118'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagem',
            name='published_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
