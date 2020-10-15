from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .models import PostBook
from .serializers import PostBookSerializer
from rest_framework import viewsets
from django_filters import rest_framework as filters


class PostBookFilter(filters.FilterSet):

    class Meta:
        model = PostBook
        fields = {
            'title': ['icontains'],
            'author': ['icontains'],
            'language': ['icontains'],
        }


class PostBookViewSet(viewsets.ModelViewSet):
    queryset = PostBook.objects.all()
    serializer_class = PostBookSerializer
    filter_class = PostBookFilter
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['published_date']
