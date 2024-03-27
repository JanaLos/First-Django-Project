# from . -> tecka znamena z tohoto adresare, * hvezdicka znamena vsechno

from django.contrib import admin
from django.urls import path
from .views import *
# from .views.forms.views import my_view


urlpatterns = [
    path('', home_page, name="home_page"),
    path('news', news, name="news"),
    path('news2', news2, name="news2"),         #news2 (bile uprostred) je nazev fce, ktera se spousti
    path('news2/super_news', super_news, name="supernews"),     #news2/super_news -> nazev stranky
    path('current_day/', current_day_of_week, name='current_day'),
    path('members', members, name='members'),
    path('phones', phones, name='phones'),
    path('details/<int:id>', details, name='details'),      #<int:id> beru cislo ktere se ulozi do ID ve views.py def details(requst, id)
    # path('', include('members.urls')),
    # path('admin/', admin.site.urls),
    path('basicform', my_view, name='basic_form'),
    path('member_form', member_form, name='member_form'),
    path('country/', adress_view2, name='adress_view2'),
    path('country/<str:city>/<int:street>', adress_view, name='adress_view')
]

