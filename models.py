# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    username = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class ProfilCategorie(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=1000)
    order = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'profil_categorie'


class ProfilProfil(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nom_organisme = models.TextField()
    nom_referent = models.TextField()
    courriel = models.CharField(max_length=254)
    adresse = models.TextField()
    mandat = models.TextField()
    objetif = models.TextField()
    personnes_impliquees = models.IntegerField()
    personnes_employees = models.IntegerField()
    personnes_moins_de_25 = models.IntegerField()
    retombees = models.TextField()
    superficie = models.IntegerField()
    adresse_jardin = models.TextField()
    city = models.CharField(max_length=255)
    location = models.CharField(max_length=63)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'profil_profil'


class ProfilProfilCategories(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    profil = models.ForeignKey(ProfilProfil, models.DO_NOTHING)
    categorie = models.ForeignKey(ProfilCategorie, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'profil_profil_categories'
        unique_together = (('profil', 'categorie'),)


class QuestionnairequalitatifGenre(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=1000)
    order = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'questionnairequalitatif_genre'


class QuestionnairequalitatifLangue(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=1000)
    order = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'questionnairequalitatif_langue'
# Unable to inspect table 'questionnairequalitatif_qualitatif_quartier'
# The error was: list index out of range


class QuestionnairequalitatifQuartierdb(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=1000)
    order = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'questionnairequalitatif_quartierdb'


class QuestionnairequalitatifQuestionnairequalitatif(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    lien = models.CharField(max_length=3)
    age = models.CharField(max_length=100)
    bien_etre = models.CharField(max_length=50)
    condition_physique_ou_cognitive = models.CharField(max_length=100)
    enfant_13_a_17 = models.CharField(max_length=1)
    enfant_5_a_8 = models.CharField(max_length=1)
    enfant_8_a_12 = models.CharField(max_length=1)
    envie_legumes = models.CharField(max_length=3)
    genre = models.ForeignKey(QuestionnairequalitatifGenre, models.DO_NOTHING)
    implication = models.CharField(max_length=3)
    langue = models.ForeignKey(QuestionnairequalitatifLangue, models.DO_NOTHING)
    nouvelle_competence = models.CharField(max_length=100)
    quartier = models.ForeignKey(QuestionnairequalitatifQuartierdb, models.DO_NOTHING)
    resident_depuis = models.CharField(max_length=100)
    revenu_annuel_familial = models.CharField(max_length=100)
    situation_familiale = models.CharField(max_length=100)
    source_revenus = models.ForeignKey('QuestionnairequalitatifSourcerevenu', models.DO_NOTHING)
    ville_origine = models.ForeignKey('QuestionnairequalitatifVilleorigine', models.DO_NOTHING)
    date = models.DateTimeField()
    nouvelle_competence_si_oui = models.CharField(max_length=1000)
    condition_physique_ou_cognitive_si_oui = models.CharField(max_length=1000)
    enfant_0_a_4 = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'questionnairequalitatif_questionnairequalitatif'


class QuestionnairequalitatifQuestionnairequalitatifRaison(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    questionnairequalitatif = models.ForeignKey(QuestionnairequalitatifQuestionnairequalitatif, models.DO_NOTHING)
    raison = models.ForeignKey('QuestionnairequalitatifRaison', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'questionnairequalitatif_questionnairequalitatif_raison'
        unique_together = (('questionnairequalitatif', 'raison'),)


class QuestionnairequalitatifRaison(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    order = models.CharField(max_length=3)
    name = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'questionnairequalitatif_raison'


class QuestionnairequalitatifSourcerevenu(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=1000)
    order = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'questionnairequalitatif_sourcerevenu'


class QuestionnairequalitatifVilleorigine(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=1000)
    order = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'questionnairequalitatif_villeorigine'


class QuestionnairequantitatifOrganisme(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=1000)
    order = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'questionnairequantitatif_organisme'


class QuestionnairequantitatifQuestionnairequantitatif(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    poids_total = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    nombre_varietes = models.IntegerField()
    nombre_personnes_toute_activite = models.IntegerField()
    nombre_educateurs = models.IntegerField()
    nombre_heures_activite = models.IntegerField()
    nombre_jardiniers = models.IntegerField()
    nombre_heures_jardins = models.IntegerField()
    nombre_benevoles = models.IntegerField()
    nombre_heures_benevoles = models.IntegerField()
    ca_total = models.IntegerField()
    ca_agriculture_urbaine = models.IntegerField()
    nombre_paniers = models.IntegerField()
    prix_panier = models.IntegerField()
    ca_semis = models.IntegerField()
    nombre_semis_rustiques = models.IntegerField()
    nombre_ruches = models.IntegerField()
    poids_miel = models.IntegerField()
    poids_composte = models.IntegerField()
    poids_pluie = models.IntegerField()
    nombre_heures_enfant = models.IntegerField()
    nombre_heures_aines = models.IntegerField()
    nombre_sujets = models.IntegerField()
    nom_organisme = models.ForeignKey(QuestionnairequantitatifOrganisme, models.DO_NOTHING, unique=True)
    date = models.DateTimeField()
    semis = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'questionnairequantitatif_questionnairequantitatif'
