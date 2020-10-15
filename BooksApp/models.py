from django.db import models
from django.utils import timezone
from django.urls import reverse


class PostBook(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.CharField(max_length=4)
    isbn_number = models.CharField(max_length=13)
    page_count = models.PositiveSmallIntegerField()
    cover_link = models.URLField()
    language = models.CharField(max_length=3)
    created_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'pk': self.pk})

    def __unicode__(self):
        return self.title
