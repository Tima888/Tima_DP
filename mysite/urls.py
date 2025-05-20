from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('news/', include('news.urls')),
    path('favors/', include('favors.urls')),
]

# Підключення статичних файлів (CSS, JS)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Підключення медіа-файлів (завантажені картинки тощо)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
