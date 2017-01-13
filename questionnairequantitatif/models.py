#-*- coding: utf-8 -*-

from django.db import models



class Organisme(models.Model):
    name = models.CharField(max_length=1000)
    order = models.CharField(max_length=3)

    def __str__(self):              # __unicode__ on Python 2
        return self.name


class Questionnairequantitatif(models.Model):
    nom_organisme = models.OneToOneField(Organisme, verbose_name="1. Nom de l’organisme :")
    poids_total = models.DecimalField(max_digits=15, decimal_places=1, verbose_name="2. Poids total des produits récoltés (en kg) :",help_text='ex format de réponse : 50.3 avec une décimale seulement', default='0')
    nombre_varietes = models.IntegerField(verbose_name="3. Nombre de variétés de plantes cultivées dans l’ensemble des jardins :",help_text='(variété = référé aux différents types d’un légume, fruit, fleur, herbe, etc. – ex : si vous cultivez des tomates cerises noires, des tomates «cœur de bœuf» et des aubergines «black beauty», vous cultivez en tout 3 variétés) (ex format de réponse : 50)', default='0')
    nombre_personnes_toute_activite = models.IntegerField(verbose_name="4. Nombre de personnes qui ont participé aux activités organisées, toutes catégories confondues ​(ateliers, jardin collectif, cuisines collectives, marché,etc.)",help_text='ex​ ​format​ ​de​ ​réponse :​ ​100)', default='0')
    nombre_educateurs = models.IntegerField(verbose_name="5. Nombre de personnes qui ont participé aux activités éducatives seulement",help_text='activité éducative = activité dirigée par une personne animatrice qui vise à développer des compétences spécifiques ou des connaissances sur un sujet en particulier chez les participants. Ex: ateliers, conférences, activités de groupe dans un jardin sur un sujet en particulier (ex format de réponse : 50)', default='0')
    nombre_heures_activite = models.IntegerField(verbose_name="6. Nombre d’heures d’activités éducatives organisées",help_text='ex format de réponse : 10', default='0')
    nombre_jardiniers = models.IntegerField(verbose_name="7. Nombre de personnes qui jardinent",help_text='peuvent être des jardiniers réguliers ou sporadiques (ex format de réponse : 30)', default='0')
    nombre_heures_jardins = models.IntegerField(verbose_name="8. Nombre d’heures passées par l’ensemble des jardiniers dans les jardins",help_text='ex format de réponse : 700', default='0')
    nombre_benevoles = models.IntegerField(verbose_name="9. Nombre total de bénévoles",help_text='bénévole = personne qui donne de son temps gratuitement pour aider au fonctionnement de l’organisme; peut être différent d’une personne qui participe aux activités de jardinage pour recevoir les produits récoltés (ex format de réponse : 50)', default='0')
    nombre_heures_benevoles = models.IntegerField(verbose_name="10. Nombre d’heures de bénévolat fournies par l’ensemble des bénévoles",help_text='ex format de réponse : 700', default='0')
    ca_total = models.IntegerField(verbose_name="11. Chiffre de ventes total du marché en dollars ($)",help_text='ex format de réponse : 25000', default='0')
    ca_agriculture_urbaine = models.IntegerField(verbose_name="12. Chiffre de ventes du marché pour les produits issus d’agriculture urbaine seulement, en dollars ($)",help_text='ex format de réponse : 10000', default='0')
    nombre_paniers = models.IntegerField(verbose_name="13. Nombre de paniers de légumes vendus",help_text='ex format de réponse : 50', default='0')
    prix_panier = models.IntegerField(verbose_name="14. Prix moyen de vente d’un panier de légumes en dollars ($)",help_text='ex format de réponse : 20', default='0')
    semis = models.IntegerField(verbose_name="15. Nombre des plantules (semis) produits",help_text='ex format de réponse : 1000', default='0')
    ca_semis = models.IntegerField(verbose_name="16. Chiffre de vente des plantules (semis) produits en dollars ($)",help_text='ex format de réponse : 3000', default='0')
    nombre_semis_rustiques = models.IntegerField(verbose_name="17. Nombre de variétés ancestrales/rustiques de plantules produits",help_text='ex format de réponse : 15', default='0')
    nombre_ruches = models.IntegerField(verbose_name="18. Nombre de ruches entretenues",help_text='ex format de réponse : 2', default='0')
    poids_miel = models.IntegerField(verbose_name="19. Quantité de miel produit en litres",help_text='ex format de réponse : 30', default='0')
    poids_composte = models.IntegerField(verbose_name="20. Poids du composte produit dans l’ensemble des jardins en kg",help_text='ex format de réponse : 1000', default='0')
    poids_pluie = models.IntegerField(verbose_name="21. Quantité d’eau de pluie ramassée en litres",help_text='ex format de réponse : 1000', default='0')
    nombre_heures_enfant = models.IntegerField(verbose_name="22. Nombre d’heures d’activités organisées spécifiquement pour les enfants",help_text='ex format de réponse : 100', default='0')
    nombre_heures_aines = models.IntegerField(verbose_name="23. Nombre d’heures d’activités organisées spécifiquement pour les personnes aînées",help_text='ex format de réponse : 100', default='0')
    nombre_sujets = models.IntegerField(verbose_name="24. Nombre de sujets différents abordés dans l’ensemble des ateliers organisés",help_text='par exemple une série d’ateliers peut porter sur : l’introduction à l’agriculture urbaine, la construction de bacs à double fond, l’introduction à la cuisine italienne – pour un total de 3 sujets abordés (ex format de réponse : 5)', default='0')
    date = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name="Date d'envoi")

    def __str__(self):              # __unicode__ on Python 2
        return self.date.strftime(' Le %d %b %Y à %Hh %Mm %Ss %Z')
