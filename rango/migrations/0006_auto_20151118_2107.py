# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0005_auto_20151118_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='url',
            field=models.URLField(),
        ),
    ]
