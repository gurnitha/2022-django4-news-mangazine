# config/urls.py

# Django modules
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    # users
    path('', include('apps.users.urls', namespace='users')),
    # newsmag
    path('', include('apps.newsmag.urls', namespace='newsmag')),
    # admin
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
