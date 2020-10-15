from django.test import TestCase
from django.urls import reverse

from .models import PostBook


class PostBookTest(TestCase):

    def create_post_book(self, title='Hobbit czyli Tam i z powrotem', author='John Ronald Reuel Tolkien',
                         published_date='1985', isbn_number='3900000459489', page_count=233,
                         cover_link='http://books.google.com/books/content?id=DqLPAAAAMAAJ&printsec=frontcover&img'
                                    '=1&zoom=5&source=gbs_api', language='en'):
        return PostBook.objects.create(title=title, authro=author, published_date=published_date,
                                       isbn_number=isbn_number, page_count=page_count, cover_link=cover_link,
                                       language=language)

    def test_post_book_create(self):
        t = self.create_post_book()
        self.assertTrue(isinstance(t, PostBook))
        self.assertEqual(t.__unicode__(), t.title)

    def test_post_book_list_view(self):
        w = self.create_post_book()
        url = reverse("BooksApp.views.BooksListView")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertIn(w.title, resp.content)
