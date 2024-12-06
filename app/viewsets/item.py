from rest_framework import viewsets
from app.models.item import Item
from app.serializers.item import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
