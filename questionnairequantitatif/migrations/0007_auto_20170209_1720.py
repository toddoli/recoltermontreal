# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-09 22:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionnairequantitatif', '0006_auto_20170209_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionnairequantitatif',
            name='nom_organisme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='1. Nom de l’organisme :'),
        ),
    ]
