from django.urls import path
from .views import CategoryListAPIView

app_name = 'categories'

urlpatterns = [
    path('', CategoryListAPIView.as_view(), name='category-list'),  # Список категорій
]


