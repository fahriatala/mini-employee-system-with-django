# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('account_type', models.CharField(max_length=20, choices=[('worker', 'Worker'), ('administrator', 'Administrator')])),
                ('account', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('information', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('information', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField(blank=True)),
                ('gender_type', models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])),
                ('worker_type', models.CharField(max_length=10, choices=[('internship', 'Internship'), ('contract', 'Contract'), ('permanent', 'Permanent')])),
                ('phonenumber', models.CharField(max_length=30, blank=True)),
                ('email', models.CharField(max_length=100)),
                ('department', models.ForeignKey(to='worker.Department')),
                ('position', models.ForeignKey(to='worker.Position')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='worker',
            field=models.ForeignKey(to='worker.Worker'),
        ),
    ]
