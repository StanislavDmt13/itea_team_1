from django.urls import path

from . import views

urlpatterns = [
    path('', views.AthleteView.as_view()),
    path('add-train/', views.TrainAddView.as_view()),
    path('edit-train/<int:pk>/', views.TrainEditView.as_view()),
    path('delete-train/<int:pk>/', views.TrainDeleteView.as_view()),
]