from django.test import TestCase, RequestFactory
from oc_lettings_site.models import Address
from .models import Letting
from .views import lettings_index, letting


class LettingViewTests(TestCase):
    """
    Tests pour les vues de locations.
    """
    def setUp(self):
        """
        Configure l'adresse et la location de test.
        """
        self.address = Address.objects.create(
            number=123,
            street="Main St",
            city="City",
            state="NY",
            zip_code=12345,
            country_iso_code="USA",
        )
        self.letting = Letting.objects.create(
            title="Test Letting", addresses=self.address
        )

    def tearDown(self):
        """
        Nettoie la location et l'adresse de test après chaque test.
        """
        self.letting.delete()
        self.address.delete()

    def test_lettings_index_view(self):
        """
        Teste que l'index des locations renvoie un statut 200
        """
        request = RequestFactory().get("/")
        response = lettings_index(request)
        self.assertEqual(response.status_code, 200)

    def test_letting_view(self):
        """
        Teste qu'une location spécifique renvoie un statut 200
        """
        request = RequestFactory().get("/")
        response = letting(request, letting_id=self.letting.id)
        self.assertEqual(response.status_code, 200)
