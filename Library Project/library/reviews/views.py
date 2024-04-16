from django.shortcuts import render, get_object_or_404
from .models import Review
from .forms import ReviewForm

def reviews(request):
    context = {
        "reviews": Review.objects.all(),
        "form": ReviewForm()
    }
    return render(request, "reviews.html", context)