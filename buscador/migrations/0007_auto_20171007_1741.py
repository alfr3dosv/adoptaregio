# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-07 17:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buscador', '0006_auto_20171007_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='fecha_publicacion',
            field=models.DateTimeField(verbose_name='fecha publicacion'),
        ),
    ]
