# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-10 22:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionnairequalitatif', '0026_auto_20170110_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qualitatif',
            name='quartier',
            field=models.ForeignKey(default='Sélectionnez', on_delete=django.db.models.deletion.CASCADE, to='questionnairequalitatif.Quartier', verbose_name='15. Quel est votre quartier de résidence?'),
        ),
    ]
