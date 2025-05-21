from django.urls import path
from . import views

urlpateterns = [
    path("", views.index, name="index"),
]