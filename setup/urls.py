from django.contrib import admin
from django.urls import path, include  # Importe o include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('devs4good.urls')),  # Inclua as URLs do seu aplicativo
]
