from django.urls import path, include

from page import views

urlpatterns = [path('', views.index, name='index')]