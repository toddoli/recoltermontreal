# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-11 04:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionnairequalitatif', '0037_auto_20170110_2344'),
    ]

    operations = [
        migrations.CreateModel(
            name='Langue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='name', max_length=1000, unique=True)),
                ('order', models.CharField(max_length=3)),
            ],
        ),
        migrations.AlterField(
            model_name='qualitatif',
            name='langue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questionnairequalitatif.Langue', verbose_name='14. Quelle langue parlez vous le plus souvent à la maison?'),
        ),
    ]
