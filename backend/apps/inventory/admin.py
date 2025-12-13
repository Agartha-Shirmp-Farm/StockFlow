from django.contrib import admin
from .models import Product, Transaction

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku', 'current_stock', 'min_stock_level', 'location')
    search_fields = ('name', 'sku')
    list_filter = ('location',)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_type', 'product', 'quantity', 'user', 'created_at')
    list_filter = ('transaction_type', 'created_at')
    search_fields = ('product__name', 'notes')
    date_hierarchy = 'created_at'
