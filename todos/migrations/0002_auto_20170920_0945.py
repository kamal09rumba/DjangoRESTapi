# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-09-20 09:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='author',
            field=models.CharField(max_length=200),
        ),
    ]