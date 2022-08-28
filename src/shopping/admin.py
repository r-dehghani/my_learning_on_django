from django.contrib import admin
from .models import User, Customer, Order, OrderItem, ShippingAddress
# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    list_display = []


admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
# admin.site.register(Product)
admin.site.register(ShippingAddress)
