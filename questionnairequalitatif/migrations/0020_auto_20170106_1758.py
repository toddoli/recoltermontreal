# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-06 22:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnairequalitatif', '0019_auto_20170106_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='categories',
            field=models.ManyToManyField(default='Sélectionnez', to='questionnairequalitatif.Categorie', verbose_name='8. Quelles sont les catégories d’activités mises sur pied par votre organisme?'),
        ),
    ]
