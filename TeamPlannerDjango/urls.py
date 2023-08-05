
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from TeamPlannerDjango import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('team/', include('main_dev.urls')),
    path('account/', include('accounts.urls')),
    path('team/team_panel/', include('to_do_list.urls')),
    path('team/team_panel/', include('projects.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)