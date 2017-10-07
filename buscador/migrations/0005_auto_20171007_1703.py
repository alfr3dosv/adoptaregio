# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-07 17:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buscador', '0004_auto_20171007_1653'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='animal',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buscador.Color'),
        ),
    ]
