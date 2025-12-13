from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    sku = models.CharField(max_length=50, unique=True)
    current_stock = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    min_stock_level = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    location = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} ({self.sku})"

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('IN', 'Stock In'),
        ('OUT', 'Stock Out'),
        ('ADJUST', 'Adjustment'),
    ]
    
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.get_transaction_type_display()} - {self.product.name} ({self.quantity})"
