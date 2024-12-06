import pytest
from app.models.item import Item


@pytest.mark.django_db
def test_item_creation() -> None:
    item = Item.objects.create(
        name="Test Item",
        description="This is a test item",
    )
    assert item.name == "Test Item"
    assert item.description == "This is a test item"
