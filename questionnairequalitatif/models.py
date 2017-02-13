#-*- coding: utf-8 -*-
from django.db import models


OUI_NON = (
    ('OUI', 'Oui'),
    ('NON', 'Non'),
)

BIEN_ETRE = (
    ('PHYSIQUE', 'Physique'),
    ('MENTAL', 'Mental'),
    ('AUCUN', 'Ni l’un ni l’autre'),
)

AGE = (
    ('MOINS_18', 'Moins de 18 ans'),
    ('18_24', '18-24'),
    ('25_34', '25-34'),
    ('35_50', '35-50'),
    ('50_64', '50-64'),
    ('65_ET_PLUS', '65 et plus'),
)

NOMBRE_0_A_9 = (
    ('0', '0'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
)

MONTANT_REVENUS = (
    ('0_10K', '0 - 9 999$'),
    ('10K_20K', '10 000$ - 19 999$'),
    ('20K_30K', '20 000$ - 29 999$'),
    ('30K_40K', '30 000$ - 39 999$'),
    ('40K_50K', '40 000$ - 49 999$'),
    ('PLUS_DE_50K', 'Plus de 50 000$'),
    ('NE_REPOND_PAS', 'Je préfère ne pas répondre'),
)

RESIDENT_DEPUIS = (
    ('PAS_RESIDENT', 'Je ne suis pas Résident'),
    ('MOINS_1_ANS',  'Moins d\'un an'),
    ('ENTRE_1_ET_2_ANS', 'Entre 1 et 2 ans'),
    ('PLUS_DE_2_ANS', 'Plus de 2 ans'),
)

SITUATION_FAMILIALE = (
    ('PERSONNE_SEULE', 'Personne seule'),
    ('COUPLE_SANS_ENFANT', 'Couple sans enfant'),
    ('COUPLE_AVEC_ENFANT', 'Couple avec enfant'),
    ('FAMILLE_MONO_PARENTALE', 'Famille mono-parentale'),
)
class Quartierdb(models.Model):
    name = models.CharField(max_length=1000, db_column='name', unique=True)
    order = models.CharField(max_length=3)

    def __str__(self):
        return self.name

class SourceRevenu(models.Model):
    name = models.CharField(max_length=1000, db_column='name', unique=True)
    order = models.CharField(max_length=3)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=1000, db_column='name', unique=True)
    order = models.CharField(max_length=3)

    def __str__(self):
        return self.name

class VilleOrigine(models.Model):
    name = models.CharField(max_length=1000, db_column='name', unique=True)
    order = models.CharField(max_length=3)

    def __str__(self):
        return self.name

class Langue(models.Model):
    name = models.CharField(max_length=1000, db_column='name', unique=True)
    order = models.CharField(max_length=3)

    def __str__(self):
        return self.name

class Raison(models.Model):
    name = models.CharField(max_length=1000)
    order = models.CharField(max_length=3)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class QuestionnaireQualitatif(models.Model):
    raison = models.ManyToManyField(Raison, verbose_name="1. Pour quelles raisons avez-vous participé à cette activité ? (plusieurs choix possibles)", default='Par souci environnemental')
    lien = models.CharField(max_length=3, choices=OUI_NON, verbose_name="2. Lors de cette activité d’agriculture urbaine, avez-vous rencontré ou tissé des liens avec une nouvelle personne?",default='Oui')
    bien_etre = models.CharField(max_length=50, choices=BIEN_ETRE, verbose_name="3. Considérez-vous que cette activité à contribué à votre bien-être?",default='Aucun')
    envie_legumes = models.CharField(max_length=3, choices=OUI_NON, verbose_name="4. Est-ce que cette activité vous a donné envie de manger plus de fruits/légumes?",default='Oui')
    nouvelle_competence = models.CharField(max_length=100, choices=OUI_NON, verbose_name="5. Avez-vous appris quelque chose de nouveau et/ou développé de nouvelles compétences suite à cette activité?",default='Oui')
    nouvelle_competence_si_oui = models.CharField(max_length=1000, verbose_name="Si 'Oui', quoi ?",blank=True)
    implication = models.CharField(max_length=3, choices=OUI_NON, verbose_name="6. Suite à cette activité, vous sentez-vous plus impliqué dans votre quartier?",default='Oui')
    genre = models.ForeignKey(Genre, verbose_name="7. Votre genre :", default='Femme')
    age = models.CharField(max_length=100, choices=AGE, verbose_name="8. Votre âge :",default='25-34')
    enfant_0_a_4 = models.CharField(max_length=1, choices=NOMBRE_0_A_9, verbose_name="9. Nombre d’enfants participants avec vous:     - enfant(s) de 0-4 ans :",default='0')
    enfant_5_a_8 = models.CharField(max_length=1, choices=NOMBRE_0_A_9, verbose_name="- enfant(s) de 5-8 ans :",default='0')
    enfant_8_a_12 = models.CharField(max_length=1, choices=NOMBRE_0_A_9, verbose_name="- enfant(s) de 8-12 ans :",default='0')
    enfant_13_a_17 = models.CharField(max_length=1, choices=NOMBRE_0_A_9, verbose_name="- enfant(s) de 13-17 ans :",default='0')
    condition_physique_ou_cognitive = models.CharField(max_length=100, choices=OUI_NON, verbose_name="10. Avez-vous une condition physique ou cognitive particulière?",default='Oui')
    condition_physique_ou_cognitive_si_oui = models.CharField(max_length=1000, verbose_name="Si 'Oui', quoi ?", blank=True )
    situation_familiale = models.CharField(max_length=100, choices=SITUATION_FAMILIALE, verbose_name="11. Quelle est votre situation familiale ?",default='Personne seule')
    source_revenus = models.ForeignKey(SourceRevenu, verbose_name="12. Quelle est votre source principale de revenu?",default='Travail')
    revenu_annuel_familial = models.CharField(max_length=100, choices=MONTANT_REVENUS, verbose_name="13. Quel est le revenu annuel familial avant impôt ?",default='0 - 9 999$')
    langue = models.ForeignKey(Langue, verbose_name="14. Quelle langue parlez vous le plus souvent à la maison?",default='Francais')
    quartier = models.ForeignKey(Quartierdb, verbose_name="15. Quel est votre quartier de résidence?", default='Ahuntsic-Cartierville')
    ville_origine =  models.ForeignKey(VilleOrigine,verbose_name="16. Où se trouve votre ville d’origine?", default='Au Quebec')
    resident_depuis = models.CharField(max_length=100, choices=RESIDENT_DEPUIS, verbose_name="17. Si vous n’êtes pas originaire de Montréal, depuis combien de temps vous y résidez?",default='Je ne suis pas Résident')
    date = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name="Date d'envoi")

    def __str__(self):              # __unicode__ on Python 2
        return self.date.strftime(' Le %d %b %Y à %Hh %Mm %Ss %Z')

