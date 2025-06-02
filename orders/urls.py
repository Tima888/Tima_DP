from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:service_id>/', views.create_order, name='create_order'),
    path('choose/', views.choose_service, name='choose_service'), 
    path('thank_you/', views.thank_you, name='thank_you'),
    path('status/', views.order_lookup, name='order_lookup'),  # форма для введення ID
    path('status/<int:order_id>/', views.order_status, name='order_status'),  # показ статусу

]
