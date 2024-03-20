from django.shortcuts import render

# Create your views here.


from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from random import choice
import datetime


# def home_page(request):
#     return HttpResponse("Hello world!")

def home_page(request):
    template = loader.get_template('home.html')       #nacte sablonu
    return HttpResponse(template.render())          #vratri rendeer -> vykresleni na stranu uzivatele



def news(request):
    template = loader.get_template('news.html')
    return HttpResponse(template.render())


def news2(request):
    template = loader.get_template('news2.html')
    sentence = choice(['veta1', 'veta2', 'veta3', 'veta4'])
    context = {
        'sentence': sentence,
    }
    return HttpResponse(template.render(context, request))



def super_news(request):
    template = loader.get_template('news2.html')
    sentence = choice(['super veta1', 'super veta2', 'super veta3', 'super veta4'])
    context = {
        'sentence': sentence,

    }
    return HttpResponse(template.render(context, request))




def current_day_of_week(request):
    # Get the current date
    current_date = datetime.datetime.now()

    # Get the day of the week (0=Monday, 1=Tuesday, ..., 6=Sunday)
    day_of_week = current_date.weekday()

    # Convert the day of the week to a string representation
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    current_day_of_week = days_of_week[day_of_week]

    return render(request, 'day_of_week.html', {'current_day_of_week': current_day_of_week})
