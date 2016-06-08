# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-08 01:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0003_glosa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='glosa',
            name='valor',
        ),
        migrations.AddField(
            model_name='glosa',
            name='egreso',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='glosa',
            name='ingreso',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='glosa',
            name='nombreDocumento',
            field=models.CharField(default=b'', max_length=300),
        ),
        migrations.AddField(
            model_name='glosa',
            name='nombreDocumentoOrig',
            field=models.CharField(default=b'', max_length=300),
        ),
    ]
