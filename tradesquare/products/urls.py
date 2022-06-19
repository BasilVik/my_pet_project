from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    # Страница со списком товаров
    path('products/', views.products_list),
    # Отдельная страница с информацией о товаре
    path('products/<int:pk>/', views.products_detail),
] 