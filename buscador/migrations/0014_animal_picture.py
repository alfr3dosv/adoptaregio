# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-07 23:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buscador', '0013_remove_picture_animal'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='picture',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='buscador.Picture'),
        ),
    ]
