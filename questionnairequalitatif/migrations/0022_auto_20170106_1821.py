# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-06 23:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnairequalitatif', '0021_auto_20170106_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='city',
            field=models.CharField(default='Montreal', max_length=255),
        ),
    ]
