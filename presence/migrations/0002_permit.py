# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0001_initial'),
        ('presence', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('presence_type', models.CharField(max_length=20, choices=[('permit', 'Permit'), ('cuti', 'Cuti')])),
                ('begin_time', models.DateField()),
                ('end_time', models.DateField()),
                ('reason', models.TextField()),
                ('approvement', models.BooleanField(default=False)),
                ('worker', models.ForeignKey(to='worker.Worker')),
            ],
        ),
    ]
