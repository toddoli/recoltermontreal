# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-06 17:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnairequalitatif', '0008_auto_20170106_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='user',
            field=models.ManyToManyField(to='questionnairequalitatif.User', verbose_name='bar'),
        ),
    ]
