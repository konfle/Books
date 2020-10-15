from django.conf.urls import url
from django.urls import path, include

from . import views
from .router import router

from .views import (
    BooksListView,
    BooksDetailView,
    BooksCreateView,
    BooksUpdateView,
    BooksDeleteView,
)

urlpatterns = [
    # BooksApp
    path('', BooksListView.as_view(), name='book_list'),
    path('book/<int:pk>/', BooksDetailView.as_view(), name='book_detail'),
    path('book/new/', BooksCreateView.as_view(), name='book_create'),
    path('book/<int:pk>/update/', BooksUpdateView.as_view(), name='book_update'),
    path('book/<int:pk>/delete/', BooksDeleteView.as_view(), name='book_delete'),
    # path('book/search/$', views.search, name='book_search'),
    url(r'^book/search/$', views.search, name='book_search'),
    # API urls
    path('api/', include(router.urls), name='book_api'),
]