
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from TeamPlannerDjango import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include('main_dev.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)