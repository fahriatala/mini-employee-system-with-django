# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presence', '0004_auto_20180716_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permit',
            name='begin_time',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='permit',
            name='end_time',
            field=models.DateField(null=True, blank=True),
        ),
    ]
