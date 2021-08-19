from django.contrib import admin
from .models import ProductData

# Register your models here.

@admin.register(ProductData)
class ProductAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'weight', 'price', 'created_at', 'updated_at']