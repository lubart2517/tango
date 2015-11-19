# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0004_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(unique=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='page',
            name='url',
            field=models.URLField(unique=True),
        ),
    ]
