from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from random import choice
import datetime
# from academy_project.company_core.models import *
from ..models import *

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

    return render(request, 'current_day.html', {'current_day_of_week': current_day_of_week})


def members(request):
  mymembers = Member.objects.all().values()     #object.all -> zadame o vsechny objekty, ktere jsou v databazi online
  template = loader.get_template('members.html')    #members.html -> nazev templatu
  context = {
      'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))


def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('detail.html')

  students = mymember.student_set.all()

  student = None
  if students:
      student = students[0]

  context = {
    'mymember': mymember,
    "student": student
  }
  return HttpResponse(template.render(context, request))


def phones(request):
  phones = Phones.objects.all().values()     #object.all -> zadame o vsechny objekty, ktere jsou v databazi online
  template = loader.get_template('phones.html')    #members.html -> nazev templatu
  context = {
    'phones': phones,
  }
  return HttpResponse(template.render(context, request))



def adress_view(request, city, street):
    # http://127.0.0.1:8000/country/hlavni/0
    cities = {"hlavni": "Praha",
              "mensi": "Brno"}

    streets = ["prvni", "druha", "treti"]

    my_city = cities.get(city)
    my_street = streets[street]

    template = loader.get_template('adress.html')
    context = {
        'city_name': my_city,
        "street": my_street
    }
    return HttpResponse(template.render(context, request))


def adress_view2(request, city, street):
    # http://127.0.0.1:8000/country/?city=hlavni&street=0
    cities = {"hlavni": "Praha",
              "mensi": "Brno"}

    streets = ["prvni", "druha", "treti"]

    my_city = cities.get(request.GET["city"])
    my_street = streets[int(request.GET["street"])]

    template = loader.get_template('adress.html')
    context = {
        'city_name': my_city,
        "street": my_street
    }
    return HttpResponse(template.render(context, request))