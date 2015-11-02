# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Propietario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rut', models.CharField(max_length=13)),
                ('nombres', models.CharField(max_length=100)),
                ('apellido_paterno', models.CharField(max_length=100)),
                ('apellido_materno', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=1, choices=[(b'M', b'Masculino'), (b'F', b'Femenino')])),
                ('fecha_ingreso', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='departamento',
            name='propietario',
            field=models.ForeignKey(to='registro.Propietario'),
        ),
    ]
