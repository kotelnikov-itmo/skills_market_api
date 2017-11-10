# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-10 21:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sm_projects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignment',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='project',
            name='end_date',
        ),
        migrations.AlterField(
            model_name='assignment',
            name='start_date',
            field=models.DateField(auto_created=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(auto_created=True),
        ),
    ]
