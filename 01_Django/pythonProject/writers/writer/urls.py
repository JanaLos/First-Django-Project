from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('writers', views.writers, name='writers'),
    path('writers/Hemingway', views.Hemingway, name='Hemingway'),
    # path('writers/Hemingway/The_Old_Man_and_the_Sea', views.Hemingway_The_Old_Man_and_the_Sea,
    #      name='Hemingway/The_Old_Man_and_the_Sea'),
    # path('writers/Hemingway/The_Sun_Also_Rises', views.Hemingway_The_Sun_Also_Rises, name='Hemingway/The_Sun_Also_Rises'),
    path('writers/', views.custom_view_year, name='custom_view_year'),      # writers/?writers=Hemingway&year=1940, writers/?writers=Hemingway&year=1926
    path('writers/Shakespeare', views.Shakespeare, name='Shakespeare'),
    path('best_books', views.best_books, name='best books'),
    # path('best_books/1', views.best_books1, name='best books1'),
    # path('best_books/2', views.best_books2, name='best books2'),
    # path('best_books/3', views.best_books3, name='best books3'),
    path('best_books/<order>', views.best_books_custom, name='best book'),
    path('writers/Hemingway/<name_of_book>', views.Hemingway_custom_book, name='custom_view_book'),
    ]


# terminal = py manage.py runserver
