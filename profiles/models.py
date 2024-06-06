from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Représente le profil utilisateur.

    Champs :
    - user : L'utilisateur auquel le profil est associé (clé étrangère vers User).
    - favorite_city : La ville préférée de l'utilisateur (chaîne de caractères, optionnelle).

    Méthodes :
    - __str__() : Renvoie une représentation de chaîne du nom d'utilisateur du profil.

    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = "profiles_profile"
