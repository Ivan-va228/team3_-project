from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/products/', include('products.urls')),  
    path('api/products/search/', views.search_products, name='search_products'),  
    path('api/categories/', include('categories.urls')), 
    path('api/brands/', include('brands.urls')),
    path('api/', include('accounts.urls')),
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('update-cart/<int:product_id>/', views.update_cart, name='update_cart'),
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.cart, name='cart'),
    path('catalog/', views.catalog, name='catalog'),
    path('like/', views.like, name='like'),
    path('account/', views.account, name='account'),
    path('register/', views.register, name='register'),
    path('products/', include('products.urls')),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
