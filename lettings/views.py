from django.shortcuts import render
from .models import Letting

#Affiche la liste de toutes les locations.Affiche la liste de toutes les locations.Affiche la liste de toutes les locations.Affiche la liste de toutes les locations.Affiche la liste de toutes les locations.Affiche la liste de toutes les locations.
def lettings_index(request):
    """
    Affiche la liste de toutes les locations.

    Paramètres :
    - request : La requête HTTP.

    Retour :
    - La page avec la liste des locations.
    """
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings_index.html", context)


def letting(request, letting_id):
    """
    Affiche les détails d'une location spécifique.

    Paramètres :
    - request : La requête HTTP.
    - letting_id : L'identifiant de la location à afficher.

    Retour :
    - La page avec les détails de la location spécifiée.
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        "title": letting.title,
        "address": letting.addresses,
    }
    return render(request, "letting.html", context)
