from .models import PostBook
import django_filters


class PostBookFilter(django_filters.FilterSet):

    class Meta:
        model = PostBook
        fields = ['title', 'author', 'language', 'published_date']
