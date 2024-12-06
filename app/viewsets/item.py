from rest_framework.viewsets import ModelViewSet
from app.models.item import Item
from app.serializers.item import ItemSerializer


class ItemViewSet(ModelViewSet[Item]):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
