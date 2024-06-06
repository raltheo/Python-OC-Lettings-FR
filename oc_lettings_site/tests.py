import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_my_view(client):
    url = reverse('lettings_index')
    response = client.get(url)
    assert response.status_code == 200
