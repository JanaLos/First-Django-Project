from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)


class Phones(models.Model):     #musime pridat novou tridu do admin.py!!!
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  # email = models.CharField(max_length=255, default='')     #NEFUNGUJE!!!!
  mobile_phone = models.IntegerField(max_length=255, default='')    #musim to zapsat do sablony phones.html {{ p.mobile_phone }} </li>

class Student(models.Model):
  #one to many
  #member bude ucitel
  #student muze mit 1 ucitele a ucitel (member) mnoho studentu
  name = models.CharField(max_length=100)
  classroom_teacher = models.ForeignKey(Member, on_delete=models.CASCADE)


class Book(models.Model):
  title = models.CharField(max_length=100)


class Esej(models.Model):
  title = models.CharField(max_length=100)


class Zak(models.Model):
  name = models.CharField(max_length=100)
  books = models.OneToOneField(Esej, on_delete=models.RESTRICT)

class Book(models.Model):
  title = models.CharField(max_length=100)


class Author(models.Model):
  name = models.CharField(max_length=100)
  books = models.ManyToManyField(Book)
