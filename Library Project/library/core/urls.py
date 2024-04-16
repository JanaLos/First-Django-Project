from django.urls import path
from .views import *
# from django.contrib.auth.views import LoginView, LogoutView   #misto Logout a LoginView pouzijeme auth_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", home_page, name="home_page"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout", auth_views.LogoutView.as_view(), name="logout"),
    path("registration/signup", home_page, name="signup"),
    path("profile/", profile, name="profile"),
]