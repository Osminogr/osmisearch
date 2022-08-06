from unicodedata import category
from rest_framework import serializers
from .models import *
from rest_framework import viewsets


    
class ProductItem_serializer(serializers.ModelSerializer):
    class Meta:
        model = ProductItem
        fields = '__all__'
        depth = 2

class Category_serializer(serializers.Serializer):
    class Meta:
        model = Category
        fields = '__all__'

class DataHub_serializer(serializers.ModelSerializer):
    class Meta:
        model = DataHub
        fields = '__all__'