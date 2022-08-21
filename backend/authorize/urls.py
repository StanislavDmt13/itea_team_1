from django.urls import path, include

from . import views

urlpatterns = [
    path('auth/', include('django.contrib.auth.urls')),
    path('registration/', views.register_request, name='registration')
]