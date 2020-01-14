from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView
import django_filters

from .models import Book, Author, BookInstance, Genre


def index(request):
    """ Функция отображения для домашней страницы сайта."""
    # Генерация "количеств" некоторых главных объектов
    num_books = Book.objects.all().count()
    num_genre = Genre.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Доступные книги (статус = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()  # Метод 'all()' применен по умолчанию.

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_books': num_books, 'num_genre': num_genre, 'num_instances': num_instances,
                 'num_instances_available': num_instances_available, 'num_authors': num_authors},
    )


# class FilteredListView(ListView):
#     # filterset_class = None
#
#     def get_queryset(self):
#         # Get the queryset however you usually would.  For example:
#         queryset = super().get_queryset()
#         # Then use the query parameters and the queryset to
#         # instantiate a filterset and save it as an attribute
#         # on the view instance for later.
#         self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
#         # Return the filtered queryset
#         return self.filterset.qs.distinct()
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # Pass the filterset to the template - it provides the form.
#         context['filterset'] = self.filterset
#         return context


class BookListView(generic.ListView):
    """Generic class-based view for a list of books."""
    # filterset_class = BookFilterset
    model = Book

class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    """Generic class-based view for a list of books."""
    model = Author
    paginate_by = 10


class AuthorDetailView(generic.DetailView):
    model = Author
