from .models import PostBook
from .forms import BooksCreateForm
from django.shortcuts import render
from .filters import PostBookFilter
from django_filters.views import FilterView
from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)


class BooksListView(FilterView):
    model = PostBook
    template_name = 'BooksApp/index.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'books'
    ordering = ['-created_date']
    filterset_fields = ['title', 'author', 'language', 'published_date']


class BooksDetailView(DetailView):
    model = PostBook


class BooksCreateView(CreateView):
    model = PostBook
    form_class = BooksCreateForm


class BooksUpdateView(UpdateView):
    model = PostBook
    form_class = BooksCreateForm


class BooksDeleteView(DeleteView):
    model = PostBook
    form_class = BooksCreateForm
    success_url = '/'

# Filter view


def search(request):
    books_list = PostBook.objects.all()
    books_filter = PostBookFilter(request.GET, queryset=books_list)
    return render(request, 'BooksApp/search.html', {'filter': books_filter})
