# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-11 05:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnairequalitatif', '0041_auto_20170111_0003'),
    ]

    operations = [
        migrations.AddField(
            model_name='qualitatif',
            name='nouvelle_competence_si_oui',
            field=models.CharField(default='', max_length=1000, verbose_name="Si 'oui', quoi ?"),
        ),
        migrations.AlterField(
            model_name='qualitatif',
            name='nouvelle_competence',
            field=models.CharField(choices=[('OUI', 'Oui'), ('NON', 'Non')], default='Sélectionnez', max_length=100, verbose_name='5. Avez-vous appris quelque chose de nouveau et/ou développé de nouvelles compétences suite à cette activité?'),
        ),
    ]
