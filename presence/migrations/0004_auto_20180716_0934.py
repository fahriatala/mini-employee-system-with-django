# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presence', '0003_auto_20180705_0701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permit',
            name='begin_time',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='permit',
            name='end_time',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
