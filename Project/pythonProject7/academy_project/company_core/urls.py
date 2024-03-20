# from . -> tecka znamena z tohoto adresare, * hvezdicka znamena vsechno

from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', home_page, name="home_page"),
    path('news', news, name="news"),
    path('news2', news2, name="news2"),         #news2 (bile uprostred) je nazev fce, ktera se spousti
    path('news2/super_news', super_news, name="supernews"),     #news2/super_news -> nazev stranky
    path('current_day/', current_day_of_week, name='current_day'),
    # path('', include('members.urls')),
    # path('admin/', admin.site.urls),
]

