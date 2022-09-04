from django.urls import path, include

urlpatterns = [
    path('athlete/', include('backend.api.athlete.urls')),
    path('', include('backend.api.core.urls'))
]