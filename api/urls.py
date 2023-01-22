from django.urls import path

from api import views

urlpatterns = [
    path('products/', views.ProductList.as_view()),
    path('products/<int:id>/', views.ProductDetail.as_view()),
    path('categories/', views.CategoryList.as_view()),
    path('categories/<int:id>/', views.CategoryDetail.as_view()),
    path('categories/<int:id>/products/', views.CategoryProductsDetail.as_view()),
]
