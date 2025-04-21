from django.contrib import admin
from .models import Customer, Product, Shipping, Payment, Order, OrderItem
# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'fullname', 'email', 'tel', 'created_at')
    search_fields = ('fullname', 'email')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')
    search_fields = ('name',)
    list_filter = ('price',)
    ordering = ('name',)

@admin.register(Shipping)
class ShippingAdmin(admin.ModelAdmin):
    list_display = ('method', 'fullname', 'tel', 'email')
    search_fields = ('fullname', 'email', 'method')
    list_filter = ('method',)
    ordering = ('method',)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('customer', 'card_no', 'payment_date', 'status')
    search_fields = ('customer__fullname', 'card_no')
    list_filter = ('status',)
    ordering = ('-payment_date',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'status', 'quantity', 'created_at', 'shipping', 'payment')
    search_fields = ('customer__fullname', 'status')
    list_filter = ('status', 'created_at')
    ordering = ('-created_at',)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'order', 'quantity', 'total_price')
    search_fields = ('order__customer__fullname', 'product__name')
    list_filter = ('product',)
    ordering = ('order__created_at',)
