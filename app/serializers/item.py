from rest_framework.serializers import ModelSerializer
from app.models.item import Item


class ItemSerializer(ModelSerializer[Item]):
    class Meta:
        model = Item
        fields = "__all__"
