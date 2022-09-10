from django.urls import path

from . import views

urlpatterns = [
    path('', views.AthleteView.as_view(), name='athlete'),
    path('edit/', views.AthleteEditView.as_view(), name='athlete-edit'),
    path('edit-train/<int:pk>/', views.TrainEditView.as_view(), name='edit-train'),
    path('delete-train/<int:pk>/', views.TrainDeleteView.as_view(), name='delete-train'),
    path('edit/avatar/', views.change_avatar, name='athlete-edit-avatar'),
    path('add-train/', views.add_train, name='add-train'),
    path('trains-user/', views.get_trains_user, name='trains-user'),
]