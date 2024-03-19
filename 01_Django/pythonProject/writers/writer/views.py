from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def writers(request):
  template = loader.get_template('writers.html')
  return HttpResponse(template.render())

def best_books(request):
  template = loader.get_template('best_books.html')
  return HttpResponse(template.render())