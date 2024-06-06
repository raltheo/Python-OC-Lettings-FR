from django.db import models
from oc_lettings_site.models import Address


class Letting(models.Model):
    """
    Représente une location.

    Champs :
    - title : Le titre de la location.
    - addresses : Une adresse associée à la location.

    Méthodes :
    - __str__() : Renvoie le titre de la location comme représentation de chaîne.

    Attributs de classe :
    - db_table : Nom de la table de base de données pour ce modèle.
    """

    title = models.CharField(max_length=256)
    addresses = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "lettings_letting"
