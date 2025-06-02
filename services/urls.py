from django.urls import path
from . import views

urlpatterns = [
    path('', views.services_list, name='services_list'),
    path('<int:service_id>/', views.service_detail, name='service_detail'),
]
