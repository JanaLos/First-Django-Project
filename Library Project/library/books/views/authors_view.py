from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from ..models import Book, Category, Author


class AuthorList(ListView):
    model = Author
    #context_object_name = 'books'
    template_name = "author_list.html"
    paginate_by = 2


class AuthorDetail(DetailView):
    model = Author
    template_name = "author_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all()
        return context