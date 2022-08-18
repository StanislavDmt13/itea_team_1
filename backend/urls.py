from django.urls import include, path

urlpatterns = [
    path('', include('backend.core.urls')),
    path('athlete/', include('backend.athlete.urls')),
    path('auth/', include('backend.authorize.urls')),
    path('registration/', include('backend.registration.urls')),
]
