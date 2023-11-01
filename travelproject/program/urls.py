from django.views.generic import TemplateView

from . import views
from django.urls import path
app_name='program'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('about', views.about, name='about'),
    path('home', views.home, name='home'),
    path('',views.demo,name='demo'),



]