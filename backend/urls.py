from django.urls import include, path

urlpatterns = [
    path('', include('backend.core.urls')),
    path('athlete/', include('backend.athlete.urls')),
    path('', include('backend.authorize.urls')),
]
