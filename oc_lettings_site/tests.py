import pytest
from django.test import RequestFactory
from .views import index, custom_404, custom_500
from .models import Address


@pytest.fixture
def sample_address():
    """
    Création une adresse de test
    L'adresse est nettoyée après le test.
    """
    address = Address.objects.create(
        number=123,
        street="Main St",
        city="City",
        state="NY",
        zip_code=12345,
        country_iso_code="USA",
    )
    yield address
    address.delete()


@pytest.mark.django_db
def test_index_view():
    """
    Teste que l'index renvoi un statut 200
    """
    request = RequestFactory().get("/")
    response = index(request)
    assert response.status_code == 200


@pytest.mark.django_db
def test_custom_404_view():
    """
    Teste que la vue custom 404 renvoie un statut 404.
    """
    request = RequestFactory().get("/nonexistent-page/")
    response = custom_404(request, Exception())
    assert response.status_code == 404


@pytest.mark.django_db
def test_custom_500_view():
    """
    Teste que la vue custom 500 renvoie un statut 500.
    """
    request = RequestFactory().get("/error-page/")
    response = custom_500(request)
    assert response.status_code == 500


@pytest.mark.django_db
def test_address_model(sample_address):
    """
    Teste le modèle d'adresse.
    Vérifie que le numéro est bonne et que la representation str de l'adresse est bonne.
    """
    assert sample_address.number == 123
    assert str(sample_address) == "123 Main St"
