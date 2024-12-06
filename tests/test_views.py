import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from app.models.item import Item

@pytest.mark.django_db
def test_item_viewset():
    client = APIClient()
    url = reverse('item-list')  # DRF auto-generated name for the viewset
    data = {"name": "View Item", "description": "From View Test"}
    response = client.post(url, data)
    assert response.status_code == 201
    assert Item.objects.count() == 1
