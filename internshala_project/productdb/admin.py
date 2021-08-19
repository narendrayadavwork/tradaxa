from django.contrib import admin

from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'weight', 'price', 'created_at', 'updated_at']
