# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-07 15:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buscador', '0002_auto_20171007_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gato',
            name='edad',
            field=models.DateTimeField(verbose_name='edad'),
        ),
        migrations.AlterField(
            model_name='perro',
            name='edad',
            field=models.DateTimeField(verbose_name='edad'),
        ),
    ]
