from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# from .models import *
import datetime
def home_page(request):
    template = loader.get_template("home.html")
    model = request.GET.get('model')
    if model:
        template = loader.get_template(f'model_{model}.html')
    return HttpResponse(template.render())

def french(request):
    template = loader.get_template("French.html")
    return HttpResponse(template.render())

def german(request):
    template = loader.get_template("German.html")
    return HttpResponse(template.render())

def spanish(request):
    template = loader.get_template("Spanish.html")
    return HttpResponse(template.render())


def toyota(request):
    template = loader.get_template("Toyota.html")
    return HttpResponse(template.render())

def honda(request):
    template = loader.get_template("Honda.html")
    return HttpResponse(template.render())

def renault(request):
    template = loader.get_template("Renault.html")
    return HttpResponse(template.render())


def current_day_of_week(request):
    current_date = datetime.datetime.now()
    day_of_week = current_date.weekday()

    # Convert the day of the week to a string representation
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    current_day_of_week = days_of_week[day_of_week]

    return render(request, 'current_day.html', {'current_day_of_week': current_day_of_week})

def monday(request):
    template = loader.get_template("Monday.html")
    return HttpResponse(template.render())



