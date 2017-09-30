# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_examplemodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ExampleModel',
        ),
    ]
