from django.urls import path
from .views import *


urlpatterns = [
#   path('<str: model>/', List.as_view()),      #obecne
    path('categories/', CategoriesList.as_view()),
    path('books/', BooksList.as_view(), name="books"),
    path('categories/', CategoriesList.as_view(), name="categories"),
    path('authors/', AuthorList.as_view(), name="authors"),
    path('book_detail/<int:id>/', bookDetail, name="book_detail"),
    path('author_detail/<int:pk>/', AuthorDetail.as_view(), name="author_detail"),
    path('category_detail/<int:id>/', categoryDetail, name="category_detail"),
]