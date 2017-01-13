# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-11 05:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionnairequantitatif', '0003_auto_20170110_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnairequantitatif',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name="Date d'envoi"),
        ),
        migrations.AlterField(
            model_name='questionnairequantitatif',
            name='ca_agriculture_urbaine',
            field=models.IntegerField(default='0', help_text='ex format de réponse : 10000', verbose_name='12. Chiffre de ventes du marché pour les produits issus d’agriculture urbaine seulement, en dollars ($)'),
        ),
        migrations.AlterField(
            model_name='questionnairequantitatif',
            name='ca_semis',
            field=models.IntegerField(default='0', help_text='ex format de réponse : 3000', verbose_name='16. Chiffre de vente des plantules (semis) produits en dollars ($)'),
        ),
        migrations.AlterField(
            model_name='questionnairequantitatif',
            name='ca_total',
            field=models.IntegerField(default='0', help_text='ex format de réponse : 25000', verbose_name='11. Chiffre de ventes total du marché en dollars ($)'),
        ),
        migrations.AlterField(
            model_name='questionnairequantitatif',
            name='nom_organisme',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='questionnairequantitatif.Organisme', verbose_name='1. Nom de l’organisme :'),
        ),
        migrations.AlterField(
            model_name='questionnairequantitatif',
            name='nombre_benevoles',
            field=models.IntegerField(default='0', help_text='bénévole = personne qui donne de son temps gratuitement pour aider au fonctionnement de l’organisme; peut être différent d’une personne qui participe aux activités de jardinage pour recevoir les produits récoltés (ex format de réponse : 50)', verbose_name='9. Nombre total de bénévoles'),
        ),
        migrations.AlterField(
            model_name='questionnairequantitatif',
            name='nombre_educateurs',
            field=models.IntegerField(default='0', help_text='activité éducative = activité dirigée par une personne animatrice qui vise à développer des compétences spécifiques ou des connaissances sur un sujet en particulier chez les participants. Ex: ateliers, conférences, activités de groupe dans un jardin sur un sujet en particulier (ex format de réponse : 50)', verbose_name='5. Nombre de personnes qui ont participé aux activités éducatives seulement'),
        ),
        migrations.AlterField(
            model_name='questionnairequantitatif',
            name='nombre_heures_activite',
            field=models.IntegerField(default='0', help_text='ex format de réponse : 10', verbose_name='6. Nombre d’heures d’activités éducatives organisées'),
        ),
        migrations.AlterField(
            model_name='questionnairequantitatif',
            name='nombre_heures_aines',
            field=models.IntegerField(default='0', help_text='ex format de réponse : 100', verbose_name='23. Nombre d’heures d’activités organisées spécifiquement pour les personnes aînées'),
        ),
        migrations.AlterField(
            model_name='questionnairequantitatif',
            name='nombre_heures_benevoles',
            field=models.IntegerField(default='0', help_text='ex format de réponse : 700', verbose_name='10. Nombre d’heures de bénévolat fournies par l’ensemble des bénévoles'),
        ),
        migrations.AlterField(
            model_name='questionnairequantitatif',
            name='nombre_heures_enfant',
            field=models.IntegerField(default='0', help_text='ex format de réponse : 100', verbose_name='22. Nombre d’heures d’activités organisées spécifiquement pour les enfants'),
        ),
        migrations.AlterField(
            model_name='questionnairequantitatif',
            name='nombre_heures_jardins',
            field=models.IntegerField(default='0', help_text='ex format de réponse : 700', verbose_name='8. Nombre d’heures passées par l’ensemble des jardiniers dans les jardins'),
        ),
        migrations.AlterField(
            model_name='questionnairequantitatif',
            name='nombre_jardiniers',
            field=models.IntegerField(default='0', help_text='peuvent être des jardiniers réguliers ou sporadiques (ex format de réponse : 30)', verbose_name='7. Nombre de personnes qui jardinent'),
        ),
        migrations.AlterField(
            model_name='questionnairequantitatif',
            name='nombre_paniers',
            field=models.IntegerField(default='0', help_text='ex format de réponse : 50', verbose_name='13. Nombre de paniers de légumes vendus'),
        ),
        migrations.AlterField(
            model_name='questionnairequantitatif',
            name='nombre_personnes_toute_activite',
            field=models.IntegerField(default='0', help_text='ex\u200b \u200bformat\u200b \u200bde\u200b \u200bréponse :\u200b \u200b100)', verbose_name='4. Nombre de personnes qui ont participé aux activités organisées, toutes catégories confondues \u200b(ateliers, jardin collectif, cuisines collectives, marché,etc.)'),
        ),
        migrations.AlterField(
            model_name='questionnairequantitatif',
            name='nombre_ruches',
            field=models.IntegerField(default='0', help_text='ex format de réponse : 2', verbose_name='18. Nombre de ruches entretenues'),
        ),
        migrations.AlterField(
            model_name='questionnairequantitatif',
            name='nombre_semis_rustiques',
            field=models.IntegerField(default='0', help_text='ex format de réponse : 15', verbose_name='17. Nombre de variétés ancestrales/rustiques de plantules produits'),
        ),
        migrations.AlterField(
            model_name='questionnairequantitatif',
            name='nombre_sujets',
            field=models.IntegerField(default='0', help_text='par exemple une série d’ateliers peut porter sur : l’introduction à l’agriculture urbaine, la construction de bacs à double fond, l’introduction à la cuisine italienne – pour un total de 3 sujets abordés (ex format de réponse : 5)', verbose_name='24. Nombre de sujets différents abordés dans l’ensemble des ateliers organisés'),
        ),
        migrations.AlterField(
            model_name='questionnairequantitatif',
            name='nombre_varietes',
            field=models.IntegerField(default='0', help_text='(variété = référé aux différents types d’un légume, fruit, fleur, herbe, etc. – ex : si vous cultivez des tomates cerises noires, des tomates «cœur de bœuf» et des aubergines «black beauty», vous cultivez en tout 3 variétés) (ex format de réponse : 50)', verbose_name='3. Nombre de variétés de plantes cultivées dans l’ensemble des jardins :'),
        ),
        migrations.AlterField(
            model_name='questionnairequantitatif',
            name='poids_composte',
            field=models.IntegerField(default='0', help_text='ex format de réponse : 1000', verbose_name='20. Poids du composte produit dans l’ensemble des jardins en kg'),
        ),
        migrations.AlterField(
            model_name='questionnairequantitatif',
            name='poids_miel',
            field=models.IntegerField(default='0', help_text='ex format de réponse : 30', verbose_name='19. Quantité de miel produit en litres'),
        ),
        migrations.AlterField(
            model_name='questionnairequantitatif',
            name='poids_pluie',
            field=models.IntegerField(default='0', help_text='ex format de réponse : 1000', verbose_name='21. Quantité d’eau de pluie ramassée en litres'),
        ),
        migrations.AlterField(
            model_name='questionnairequantitatif',
            name='poids_total',
            field=models.DecimalField(decimal_places=1, default='0', help_text='ex format de réponse : 50.3 avec une décimale seulement', max_digits=15, verbose_name='2. Poids total des produits récoltés (en kg) :'),
        ),
        migrations.AlterField(
            model_name='questionnairequantitatif',
            name='prix_panier',
            field=models.IntegerField(default='0', help_text='ex format de réponse : 20', verbose_name='14. Prix moyen de vente d’un panier de légumes en dollars ($)'),
        ),
        migrations.AlterField(
            model_name='questionnairequantitatif',
            name='semis',
            field=models.IntegerField(default='0', help_text='ex format de réponse : 1000', verbose_name='15. Nombre des plantules (semis) produits'),
        ),
    ]
