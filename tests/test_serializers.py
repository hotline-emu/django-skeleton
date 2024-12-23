import pytest
from app.serializers.item import ItemSerializer


@pytest.mark.django_db
def test_item_serializer() -> None:
    data = {"name": "Test Item", "description": "Test Description"}
    serializer = ItemSerializer(data=data)
    assert serializer.is_valid()
    item = serializer.save()
    assert item.name == "Test Item"
    assert item.description == "Test Description"
