# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-07 22:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buscador', '0010_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to='buscador/static'),
        ),
    ]