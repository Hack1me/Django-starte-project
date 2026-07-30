from django.db import models

# Create your models here.

class Produits(models.Model):
    nom_p = models.CharField(max_length=50)
    prix = models.PositiveIntegerField()
    qte = models.PositiveIntegerField()
    date_insert = models.DateField(null=True)

    class Meta:
        ordering = ['nom_p']

    def __str__(self):
        return self.nom_p