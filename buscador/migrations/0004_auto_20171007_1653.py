# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-07 16:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buscador', '0003_auto_20171007_1529'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('edad', models.DateTimeField(verbose_name='edad')),
                ('color', models.CharField(max_length=50)),
                ('peso', models.IntegerField(default=0)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Gato',
        ),
        migrations.DeleteModel(
            name='Perro',
        ),
        migrations.AddField(
            model_name='animal',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buscador.Mascota'),
        ),
    ]
