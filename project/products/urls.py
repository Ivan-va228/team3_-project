
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListAPIView.as_view(), name='product_list'),
    path('<int:id>/', views.ProductDetailAPIView.as_view(), name='product_detail'),
    path('search/', views.ProductSearchAPIView.as_view(), name='product_search'),
]
