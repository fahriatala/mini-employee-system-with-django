# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presence', '0002_permit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permit',
            name='presence_type',
            field=models.CharField(max_length=20, choices=[('permit', 'Permit'), ('leave', 'Leave')]),
        ),
    ]
