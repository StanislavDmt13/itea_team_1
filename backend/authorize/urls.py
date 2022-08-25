from django.urls import include, path

from . import views

urlpatterns = [
    path("auth/", include("django.contrib.auth.urls")),
    path("registration/", views.register_request, name="registration"),
]
