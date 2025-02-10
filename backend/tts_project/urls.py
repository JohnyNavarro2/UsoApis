from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tts_api.urls')),  # Agrega la ruta de la app
]
