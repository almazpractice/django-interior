from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('main.urls', namespace='interior')),
    path('admin/', admin.site.urls),
]
