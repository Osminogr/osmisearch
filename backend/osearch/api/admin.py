from django.contrib import admin
from .models import *

@admin.register(DataHub)
class DataHubAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(ProductItem)
class ProductItemAdmin(admin.ModelAdmin):
    pass