from django.urls import path
from .views import *
from django.views.generic.list import ListView


urlpatterns = [
    path('rev/', reviews, name="reviews"),
    #path('rev/', ListView.as_view(model=Review, template_name="reviews.html")),
]