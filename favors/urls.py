from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.favors, name='favors_home'),
    path('<int:equipment_id>/', views.equipment_detail, name='equipment_detail')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

