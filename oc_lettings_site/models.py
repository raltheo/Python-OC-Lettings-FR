from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Représente une adresse.

    Champs :
    - number : Le numéro de l'adresse (entier positif inférieur ou égal à 9999).
    - street : Le nom de la rue.
    - city : Le nom de la ville.
    - state : Le code de l'État (2 caractères).
    - zip_code : Le code postal (entier positif inférieur ou égal à 99999).
    - country_iso_code : Le code ISO du pays (3 caractères).

    Méthodes :
    - __str__() : Renvoie une représentation de chaîne de l'adresse.

    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        return f"{self.number} {self.street}"
