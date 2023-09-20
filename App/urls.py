from django.contrib import admin
from django.urls import path
from .views import about_view

urlpatterns = [
    path('about/', about_view),
]
