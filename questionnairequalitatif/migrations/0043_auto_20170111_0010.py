# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-11 05:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnairequalitatif', '0042_auto_20170111_0007'),
    ]

    operations = [
        migrations.AddField(
            model_name='qualitatif',
            name='condition_physique_ou_cognitive_si_oui',
            field=models.CharField(default='', max_length=1000, verbose_name="Si 'Oui', quoi ?"),
        ),
        migrations.AlterField(
            model_name='qualitatif',
            name='condition_physique_ou_cognitive',
            field=models.CharField(choices=[('OUI', 'Oui'), ('NON', 'Non')], default='Sélectionnez', max_length=100, verbose_name='10. Avez-vous une condition physique ou cognitive particulière?'),
        ),
        migrations.AlterField(
            model_name='qualitatif',
            name='nouvelle_competence_si_oui',
            field=models.CharField(default='', max_length=1000, verbose_name="Si 'Oui', quoi ?"),
        ),
    ]
