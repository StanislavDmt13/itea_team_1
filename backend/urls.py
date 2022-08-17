from django.urls import include, path

urlpatterns = [
    path('athlete/', include('backend.athlete.urls')),
    path('authorise/', include('backend.authorize.urls')),
    path('', include('backend.core.urls')),
    path('registration/', include('backend.registration.urls')),
]
