from django.shortcuts import render


def index(request):
    """
    Affiche la page d'accueil.

    Paramètres :
    - request : La requête HTTP.

    Retour :
    - La page d'accueil.
    """
    return render(request, "index.html")


def custom_404(request, exception):
    """
    Affiche la page d'erreur 404.

    Paramètres :
    - request : La requête HTTP.
    - exception : L'exception 404.

    Retour :
    - La page d'erreur 404.
    """
    return render(request, "404.html", status=404)


def custom_500(request):
    """
    Affiche la page d'erreur 500.

    Paramètres :
    - request : La requête HTTP.

    Retour :
    - La page d'erreur 500.
    """
    return render(request, "500.html", status=500)

def trigger_500(request):
    return 1 / 0
