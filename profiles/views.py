from django.shortcuts import render
from .models import Profile


def profiles_index(request):
    """
    Affiche la liste de tous les profils.

    Paramètres :
    - request : La requête HTTP.

    Retour :
    - La page avec la liste des profils.
    """
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles_index.html", context)


def profile(request, username):
    """
    Affiche le profil d'un utilisateur spécifique.

    Paramètres :
    - request : La requête HTTP.
    - username : Le nom d'utilisateur du profil à afficher.

    Retour :
    - La page de profil de l'utilisateur spécifié.
    """
    profile = Profile.objects.get(user__username=username)
    context = {"profile": profile}
    return render(request, "profile.html", context)
