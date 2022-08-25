from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("train/", views.train, name="train"),
    path("train-program/", views.train_program, name="train-program"),
]
