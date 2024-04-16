from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView
from ..models import Category, Book


class CategoriesList(ListView):
    model = Category
    #context_object_name = 'categories'
    template_name = "category_list.html"
    paginate_by = 2             #kolik veci ma byt na listu

def categoryDetail(request, id):
    print("HERE ", id)
    category = get_object_or_404(Category, pk=id)
    context = {
        "category": category,
        'books': Book.objects.filter(category=category)
    }

    return render(request, "category_detail.html", context)