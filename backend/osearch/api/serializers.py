from unicodedata import category
from rest_framework import serializers
from .models import *
from rest_framework import viewsets

class Category_serializer(serializers.Serializer):
    class Meta:
        model = Category
        fields = '__all__'
    

class CategoryListingField(serializers.RelatedField):
 
     def to_representation(self, value):
         return value.name

class ProductItem_serializer(serializers.ModelSerializer):
    categories = Category_serializer()

    class Meta:
        model = ProductItem
        fields = '__all__'
        depth = 2

class DataHub_serializer(serializers.ModelSerializer):
    class Meta:
        model = DataHub
        fields = '__all__'