# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_examplemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examplemodel',
            name='model_pic',
            field=models.ImageField(default='/media/xx.jpg', upload_to='/media/'),
        ),
    ]
