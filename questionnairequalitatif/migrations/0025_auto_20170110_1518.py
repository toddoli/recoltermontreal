# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-10 20:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionnairequalitatif', '0024_remove_profil_inscrit_newsletter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profil',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='profil',
            name='user',
        ),
        migrations.DeleteModel(
            name='Categorie',
        ),
        migrations.DeleteModel(
            name='Profil',
        ),
    ]
