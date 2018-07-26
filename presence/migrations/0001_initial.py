# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Presence',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('presence_type', models.CharField(max_length=20, choices=[('permit', 'Permit'), ('leave', 'Leave'), ('noreason', 'No Reason'), ('present', 'Present')])),
                ('time', models.DateField()),
                ('worker', models.ForeignKey(to='worker.Worker')),
            ],
        ),
    ]
