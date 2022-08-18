from django.urls import path

from . import views

urlpatterns = [
    path('', views.AthleteView.as_view(), name='athlete'),
    path('edit/', views.AthleteEditView.as_view(), name='athlete-edit'),
    path('edit/avatar/', views.change_avatar, name='athlete-edit-avatar'),
]