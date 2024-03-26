from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)


class Phones(models.Model):     #musime pridat novou tridu do admin.py!!!
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  # email = models.EmailField(max_length=255, default='')     NEFUNGUJE!!!!
  mobile_phone = models.CharField(max_length=255, default='')
