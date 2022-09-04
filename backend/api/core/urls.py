from django.urls import path

from . import views

urlpatterns = [
    path('trains/', views.TrainsListView.as_view()),
    path('trains/<int:pk>/', views.TrainView.as_view()),
]