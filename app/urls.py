from rest_framework.routers import DefaultRouter
from app.viewsets.item import ItemViewSet

router = DefaultRouter()
router.register(r'items', ItemViewSet, basename="item")

urlpatterns = router.urls
