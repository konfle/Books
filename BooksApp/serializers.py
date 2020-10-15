from .models import PostBook
from rest_framework import serializers


class PostBookSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PostBook
        fields = ['title', 'author', 'published_date', 'isbn_number', 'page_count', 'cover_link', 'language']
