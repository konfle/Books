from rest_framework import routers

from .viewsets import PostBookViewSet

router = routers.DefaultRouter()
router.register('books', PostBookViewSet)
