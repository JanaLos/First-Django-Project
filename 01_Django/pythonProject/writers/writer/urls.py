from django.urls import path
from . import views

urlpatterns = [
    path('writers', views.writers, name='writers'),
    path('', views.main, name='main'),
    path('best_books', views.best_books, name='best books')
]