# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-07 23:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionnairequantitatif', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionnairequantitatif',
            name='nom_organisme',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='questionnairequantitatif.Organisme', verbose_name='1. Nom de l’organisme :'),
        ),
    ]