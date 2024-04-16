from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from ..models import Book, Category, Author
from django.template import loader
from django.shortcuts import render, get_object_or_404


class BooksList(ListView):
    model = Book
    #context_object_name = 'books'
    template_name = "list.html"
    paginate_by = 2


    """def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         context["list_name"] = "Knihy"
         context["url_name"] = "book_detail"
         print(context)"""


def bookDetail(request, id):
    book = get_object_or_404(Book, pk=id)
    context = {
        "book": book,
        'categories': Category.objects.all(),
        "authors": Author.objects.all(),
    }

    return render(request, "book_detail.html", context)