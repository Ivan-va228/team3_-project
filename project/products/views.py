
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework.filters import SearchFilter
from rest_framework.exceptions import NotFound
from django.shortcuts import render


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'  

class ProductSearchAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (SearchFilter,)
    search_fields = ['name']  

    def get_queryset(self):
        """
        Optionally restricts the returned products to a given search query,
        by filtering against a `q` query parameter in the URL.
        """
        queryset = super().get_queryset()
        query = self.request.query_params.get('q', None)
        if query:
            queryset = queryset.filter(name__icontains=query)  
        else:
            raise NotFound("No search query provided.")
        return queryset

    