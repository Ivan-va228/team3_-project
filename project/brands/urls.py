from django.urls import path
from .views import BrandListCreateAPIView

app_name = 'brands'

urlpatterns = [
    path('', BrandListCreateAPIView.as_view(), name='brand-list-create'),
]



