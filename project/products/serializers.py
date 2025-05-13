from rest_framework import serializers
from .models import Product
from categories.models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name'] 

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)  

    class Meta:
        model = Product
        fields = '__all__' 
