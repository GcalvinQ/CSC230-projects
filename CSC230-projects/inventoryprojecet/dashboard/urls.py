from django.urls import path, include
from . import views
from booking_app.views import *

urlpatterns = [
    path('staff/', views.staff, name='dashboard-staff'),
    path('product/', views.product, name='dashboard-product'),
    path('order/', views.order, name='dashboard-order'),
    
]