from django.db import models
from django_mongodb_backend import fields


class GareIDF(models.Model):
    id = fields.ObjectIdAutoField(primary_key=True, db_column="_id")

    geo_point = models.CharField(max_length=100, db_column="Geo Point")

    geo_shape = models.TextField(db_column="Geo Shape")
    picto_ligne = models.URLField(max_length=500, db_column="picto ligne")

    objectid_1 = models.IntegerField(db_column="OBJECTID_1")
    gares_id = models.IntegerField()
    id_ref_zdc = models.IntegerField(db_column="id_ref_ZdC")
    id_ref_zda = models.IntegerField(db_column="id_ref_ZdA")

    nom_long = models.CharField(max_length=255)
    nom_so_gar = models.CharField(max_length=255, blank=True)
    nom_su_gar = models.CharField(max_length=255, blank=True)
    nom_zdc = models.CharField(max_length=255, db_column="nom_ZdC")
    nom_zda = models.CharField(max_length=255, db_column="nom_ZdA")
    nom_iv = models.CharField(max_length=255)

    # Informations lignes et réseaux
    idrefliga = models.CharField(max_length=50)
    idrefligc = models.CharField(max_length=50)
    res_com = models.CharField(max_length=100)
    indice_lig = models.CharField(max_length=10)
    mode = models.CharField(max_length=50)
    exploitant = models.CharField(max_length=100)

    tertrain = models.IntegerField()
    terrer = models.IntegerField()
    termetro = models.IntegerField()
    tertram = models.IntegerField()
    terval = models.IntegerField()
    idf = models.IntegerField()
    principal = models.IntegerField()

    x = models.FloatField()
    y = models.FloatField()

    class Meta:
        db_table = "jeu_des_trains_collections"
        managed = False
        verbose_name = "Gare Île-de-France"
        verbose_name_plural = "Gares Île-de-France"

    def __str__(self):
        return f"{self.nom_long} ({self.res_com})"
