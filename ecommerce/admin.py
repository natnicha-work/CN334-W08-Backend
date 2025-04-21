from django.contrib import admin
from .models import Customer
# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'tel', 'email', 'address')
    search_fields = ('user__username', 'user__fullname', 'tel', 'email')
    list_filter = ('user',)
    ordering = ('id',)
