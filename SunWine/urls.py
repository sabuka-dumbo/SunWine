from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from SunWineapp import views

handler404 = views.error_view
handler500 = views.error_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("SunWineapp.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    # For production (DEBUG=False), media files need to be served by your web server (e.g. nginx).
    # During development without DEBUG, Django serves media files automatically via the above.
    # But if you want to serve media via Django in production (not recommended), add this line:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
