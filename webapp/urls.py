from django.urls import path
from webapp.views import (product_view, products_view, product_add_view, category_add_view, product_edit_view,
                          product_delete_view)

urlpatterns = [
    path('', products_view, name='product_list'),
    path('products/', products_view, name='product_list'),
    path('products/<int:pk>/', product_view, name='product_detail'),
    path('products/add/', product_add_view, name='product_add'),
    path('categories/add/', category_add_view, name='category_add'),
    path('products/<int:pk>/edit/', product_edit_view, name='product_edit'),
    path('products/<int:pk>/delete/', product_delete_view, name='product_delete'),
]
