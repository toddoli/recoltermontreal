# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-07 20:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0002_auto_20170207_1458'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profil',
            old_name='objetif',
            new_name='objectif',
        ),
    ]