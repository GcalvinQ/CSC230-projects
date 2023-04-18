from django.urls import path, include
from . import views
from booking_app.views import *

urlpatterns = [
    path('dashboard/', views.index, name='dashboard-index'),
    path('staff/', views.staff, name='dashboard-staff'),
    path('product/', views.product, name='dashboard-product'),
    path('order/', views.order, name='dashboard-order'),
    path('product/delete/<int:pk>/', views.product_delete, name='dashboard-product-delete'),
    path('order/delete/<int:pk>/', views.order_delete, name='dashboard-order-delete'),
]