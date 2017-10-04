# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-08-05 16:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mibcolaboradores', '0002_auto_20170802_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaborador',
            name='colaborador_admissao',
            field=models.DateField(default=datetime.date(2017, 8, 5), verbose_name='Data de Admissão'),
        ),
        migrations.AlterField(
            model_name='franquia',
            name='franquia_funcao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mibcolaboradores.Funcao', unique=True),
        ),
    ]
