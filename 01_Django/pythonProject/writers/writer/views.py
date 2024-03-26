from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def writers(request):
  template = loader.get_template('writers.html')
  return HttpResponse(template.render())

def Hemingway(request):
  template = loader.get_template('Hemingway.html')
  return HttpResponse(template.render())

def Shakespeare(request):
  template = loader.get_template('Shakespeare.html')
  return HttpResponse(template.render())

# def Hemingway_The_Old_Man_and_the_Sea(request):
#   template = loader.get_template('Hemingway_The_Old_Man_and_the_Sea.html')
#   return HttpResponse(template.render())
#
# def Hemingway_The_Sun_Also_Rises(request):
#   template = loader.get_template('Hemingway_The_Sun_Also_Rises.html')   #book = request.GET.get('book') (f'Hemingway_{book}.html')
#   return HttpResponse(template.render())

def Hemingway_custom_book(request, name_of_book):
  # name_of_book = request.GET.get('name_of_book')  #proc se nepouzije?
  template = loader.get_template((f'Hemingway_{name_of_book}.html'))
  return HttpResponse(template.render())

# def Hemingway_1926(request):
#   template = loader.get_template('Hemingway_1926.html')
#   return HttpResponse(template.render())
#
# def Hemingway_1940(request):
#   template = loader.get_template('Hemingway_1940.html')
#   return HttpResponse(template.render())

  def custom_view_year(request):
    # writers = request.GET.get('writers')        > obecne i pro Shakespeara
    year = request.GET.get('year')

    template = loader.get_template(f'Hemingway_{year}.html')      #(f'{writers}_{year}.html') -> obecne i pro Shakespeara
    return HttpResponse(template.render())


def best_books(request):
  template = loader.get_template('best_books.html')
  return HttpResponse(template.render())

# def best_books1(request):
#   template = loader.get_template('best_books1.html')
#   return HttpResponse(template.render())
#
# def best_books2(request):
#   template = loader.get_template('best_books2.html')
#   return HttpResponse(template.render())
#
# def best_books3(request):
#   template = loader.get_template('best_books3.html')
#   return HttpResponse(template.render())

def best_books_custom(request, order):
  template = loader.get_template(f'best_books{order}.html')
  return HttpResponse(template.render())